from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from core.models import Fund
# TestCase - normal django tests
# TransactionTestCase - for code that don't use auto commit
# LiveServerTestCase - mostly for selenium 

class FirstTest(APITestCase):

    def test_fetch(self):
        client = APIClient()
        #  Make sure that the database is empty of Fund records when we start
        # testing. And if that is the case the response for the api end point
        # should also be empty.
        response = client.get('/api/funds/')
        self.assertEquals(200, response.status_code)
        data = response.json()
        self.assertEquals(0, len(data))

        # Make sure that the API returns data added to database
        Fund.objects.create(name="First1")
        response = client.get('/api/funds/')
        self.assertEquals(200, response.status_code)
        data = response.json()
        self.assertEquals(1, len(data))
        self.assertEquals('First1', data[0]['name'])

        # Make sure API accepts/ rejects icnorrectly formatted data
    def test_create(self):
        self.assertEquals(0, Fund.objects.count())   

        client = APIClient()
        response = client.post('/api/funds/', {'name': 'posted'})
        self.assertEquals(201, response.status_code)
        self.assertEquals(1, Fund.objects.count())


        client = APIClient()
        response = client.post('/api/funds/', {'NAME': 'posted'})
        self.assertEquals(400, response.status_code)
        self.assertEquals(1, Fund.objects.count())
         