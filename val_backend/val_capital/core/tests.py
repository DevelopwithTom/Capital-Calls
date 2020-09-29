from django.test import TestCase
from core.models import Fund, Commitment, Call, Drawdown


class ModelTests(TestCase):

    def helper(self):
        Fund.objects.create(name='33')

    
    def test_create_commitment(self):
        self.helper()
        c = Commitment(fund=Fund.objects.all()[0], 
           amount = 1000, date ='2020-09-29')

        self.assertEquals(None, c.undrawn)
        self.assertEquals(1000, c.amount)

        c.save()

        from_db = Commitment.objects.all()[0]
        self.assertEquals(1000, c.undrawn)

    def test_create_call_1(self):
        self.helper()
        call = Call(amount = 1000, date ='2020-09-29')
        call.save()
        self.assertEquals(1, Call.objects.count())
        self.assertEquals(0, Drawdown.objects.count())

        com = Commitment(fund=Fund.objects.all()[0], 
           amount = 1000, date ='2020-09-29')
        com.save()
        call = Call(amount = 100, date ='2020-09-29')
        call.save()
        self.assertEquals(2, Call.objects.count())
        self.assertEquals(1, Drawdown.objects.count())
        
    def test_create_call_2(self):
        self.helper()
   
        com = Commitment(fund=Fund.objects.all()[0], 
           amount = 1000, date ='2020-09-29')
        com.save()
        call = Call(amount = 1100, date ='2020-09-29')
        call.save()
        self.assertEquals(1, Call.objects.count())
        self.assertEquals(1, Drawdown.objects.count())
        
        from_db = Commitment.objects.all()[0]
        self.assertEquals(0, from_db.undrawn)
        self.assertEquals(1000, from_db.amount)

