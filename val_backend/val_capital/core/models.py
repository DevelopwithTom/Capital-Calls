from django.db import models

class Fund(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "Fund ID %s: %s" %(self.id, self.name)

    class Meta:
        ordering = ['id']


class Commitment(models.Model):
    fund = models.ForeignKey(Fund, on_delete=models.PROTECT)
    date = models.DateField()
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    undrawn = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Undrawn Capital", blank=True)

    def __str__(self):
        return "Fund: %s, Amount: %s" %(self.fund.name, self.amount)

    def save(self, **kwargs):
        if not self.pk and not self.undrawn:
            self.undrawn = self.amount

        super().save(**kwargs)

    class Meta:
        ordering = ['date']



class Call(models.Model):
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    date = models.DateField()
    # Call and commitment have a many-to-many relationship through drawdown. Read up on many-to-many relatioships

    def __str__(self):
        return "Call ID: %s, Amount: %s" %(self.id, self.amount)

    def save(self, **kwargs):
        if not self.pk:
            amount = self.amount
            drawdowns = []
            for commitment in Commitment.objects.order_by("date"):
                if commitment.undrawn > 0:
                    if amount > commitment.undrawn:
                        drawdown = Drawdown(commitment=commitment, amount=commitment.amount)
                        drawdowns.append(drawdown)
      
                        amount -= commitment.undrawn
                        commitment.undrawn = 0
                        commitment.save()
                    else:
                       
                        drawdown = Drawdown(commitment=commitment, amount=amount)
                        drawdowns.append(drawdown)
                        commitment.undrawn -= amount
                        amount = 0
                        commitment.save()
                    if amount == 0:
                        break

        super().save(**kwargs)
        for c in drawdowns:
            c.call = self
            c.date = self.date
        Drawdown.objects.bulk_create(drawdowns)


class Drawdown(models.Model):
    call = models.ForeignKey(Call, on_delete=models.PROTECT) 
    commitment = models.ForeignKey(Commitment, on_delete=models.PROTECT)
    date = models.DateField()
    amount = models.DecimalField(max_digits=14, decimal_places=2)

    def __str__(self):
        return "%s, Amount %s" %(self.call, self.amount)


    class Meta:
        ordering = ['id']

