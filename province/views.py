from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from province.models import ProvinceModel

class ProvinceAPIView(APIView):
    def get(self, request):
        api_url = "https://api.rajaongkir.com/starter/province"
        headers = {
            'Content-Type': 'application/json',
            'key': '36e7a7e86fb50a3e4c60140d0a35bb8a'
        }
        
        try:
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200 :
                response = response.json()
                data_province = response['rajaongkir']['results']        
                # for item in data_province:
                #     ProvinceModel.objects.create(
                #         province_id = item['province_id'],
                #         province = item['province'],
                #     )
                return Response(data_province, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'not found'}, status=status.HTTP_404_NOT_FOUND)
            
        except requests.exceptions.HTTPError as e:
            return Response({'error':e})
            

