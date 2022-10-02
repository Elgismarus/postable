from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from postalcode import valid_postal_code, Countries

class PostalCodeDetailView(APIView):
    def get(self, request, country, code):
        '''
        Check if postal code provided exist

        :param  Request     request     REST request
        :param  str         country     Country code
        :param  str         code        Postal code
        :return:
            - OK (200) if postal code found
            - NOT_FOUND (404) if invalid postal code
        '''
        if valid_postal_code(country, code):
            # Just return blank body. OK status will
            # indicate exist.
            # Body could return specification from postal
            # code
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)
