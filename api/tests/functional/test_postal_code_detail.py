from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from api.views import PostalCodeDetailView

class TestPostalCodeDetail(APITestCase):
    '''
    Test for GET /postalcode/:country/:code
    '''

    def send_request(self, country, code):
        '''
        Send request for specific country and postal code

        :param  str     country     The country code
        :param  str     code        The postal code
        :return:    Response
        '''
        request = self.factory.get(
            self.uri,
            country=country,
            code=code
        )
        return self.view(request, country = country, code = code)

    def setUp(self):
        '''
        Setup reusable in test
        '''
        self.uri = '/postalcode/'
        self.view = PostalCodeDetailView.as_view()
        self.factory = APIRequestFactory()

    def test_should_return_200_if_valid(self):
        '''
        Test return OK (200) if postal code valid
        '''
        country = 'UK'
        code = 'EC1A 1BB'
        response = self.send_request(country, code)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_return_404_if_invalid(self):
        '''
        Test return NOT_FOUND (404) if postal code invalid
        '''
        country = 'UK'
        code = 'HHHdd'
        response = self.send_request(country, code)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
