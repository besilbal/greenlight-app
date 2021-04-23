from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from random import randint


# Create your views here.
class DemoApi(APIView):

    def get(self, request):
        num = randint(00, 99)
        if num % 2 == 0:
            return Response(data={'message': True}, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': False}, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            data = request.data
            msg = data['msg']
            return Response(data={'message': f'data stored - {msg}'}, status=status.HTTP_201_CREATED)
        except KeyError as error:
            return Response(data={'message': f'{error} key missing'}, status=status.HTTP_400_BAD_REQUEST)
