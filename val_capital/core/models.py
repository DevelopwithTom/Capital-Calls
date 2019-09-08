from django.db import models

class Fund(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "Fund ID %s: %s" %(self.id, self.name)

    class Meta:
        ordering = ['id']


class Deposit(models.Model):
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
        ordering = ['id']

   



class Call(models.Model):
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    date = models.DateField()
    # Call and deposit have a many-to-many relationship through Commitment. Read up on many-to-many relatioships

    def __str__(self):
        return "Call ID: %s, Amount: %s" %(self.id, self.amount)

    def save(self, **kwargs):
        if not self.pk:
            amount = self.amount
            commitments = []
            for deposit in Deposit.objects.all():
                if deposit.undrawn > 0:
                    if amount > deposit.undrawn:
                        commitment = Commitment(deposit=deposit, amount=deposit.amount)
                        commitments.append(commitment)
      
                        amount -= deposit.undrawn
                        deposit.undrawn = 0
                        deposit.save()
                    else:
                        commitment = Commitment(deposit=deposit, amount=amount)
                        commitments.append(commitment)
                        deposit.undrawn -= amount
                        amount = 0
                        deposit.save()
                    if amount == 0:
                        break

        super().save(**kwargs)
        for c in commitments:
            c.call = self
            c.date = self.date
        Commitment.objects.bulk_create(commitments)


class Commitment(models.Model):
    call = models.ForeignKey(Call, on_delete=models.PROTECT) 
    deposit = models.ForeignKey(Deposit, on_delete=models.PROTECT)
    date = models.DateField()
    amount = models.DecimalField(max_digits=14, decimal_places=2)

    def __str__(self):
        return "%s, Amount %s" %(self.call, self.amount)


    class Meta:
        ordering = ['id']

