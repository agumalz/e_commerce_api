from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProductModel
from .serializers import ProductSerializer
from utils.response_json import CustomResponseJson

class ProductListView(APIView):
    def get(self, request):
        products = ProductModel.objects.all()
        serializer = ProductSerializer(products, many=True)
        return CustomResponseJson(statusCode=status.HTTP_200_OK, data=serializer.data).generate_success_json()
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponseJson(statusCode=status.HTTP_201_CREATED, data=serializer.data).generate_success_json()
        else:
            return CustomResponseJson(statusCode=status.HTTP_400_BAD_REQUEST, data={'error': 'Invalid data'}).generate_error_json()

class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = ProductModel.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return CustomResponseJson(statusCode=status.HTTP_200_OK, data=serializer.data).generate_success_json()
        except ProductModel.DoesNotExist:
            return CustomResponseJson(statusCode=status.HTTP_404_NOT_FOUND, data={'error': 'Category not found'}).generate_error_json()
        
    def delete(self, request, pk):
        try:
            product = ProductModel.objects.get(pk=pk)
            product.delete()
            return Response({
                'status':'success',
                'message':'Product deleted!'
            }, status=status.HTTP_200_OK)
            
        except ProductModel.DoesNotExist:
            return CustomResponseJson(statusCode=status.HTTP_404_NOT_FOUND, data={'error': 'Category not found'}).generate_error_json()
        
    def put(self, request, pk):
        try:
            product = ProductModel.objects.get(pk=pk)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':'success',
                    'message':'Product edited!'
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'status':'error',
                    'message':'Invalid data'
                }, status=status.HTTP_400_BAD_REQUEST)
                
        except ProductModel.DoesNotExist:
            return CustomResponseJson(statusCode=status.HTTP_404_NOT_FOUND, data={'error': 'Product not found'}).generate_error_json()