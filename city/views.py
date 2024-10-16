from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from city.models import CityModel

class CityAPIView(APIView):
    def get(self, request):
        api_urls = 'https://api.rajaongkir.com/starter/city'
        headers = {
            'Content-Type': 'application/json',
            'key': '36e7a7e86fb50a3e4c60140d0a35bb8a'
        }
        
        try:
            response = requests.get(api_urls, headers=headers)
            if response.status_code == 200:
                response = response.json()
                data_city = response ['rajaongkir']['results']
                
                # for item in data_city:
                #     CityModel.objects.create(
                #         city_id = item['city_id'],
                #         city_name = item['city_name'],
                #         province = item['province'],
                #         type = item['type'],
                #         postal_code = item['postal_code']
                #     )
                return Response(data_city, status=status.HTTP_200_OK)
            else:
                return Response({'message':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except requests.exceptions.HTTPError as e:
            return Response({'error':e})