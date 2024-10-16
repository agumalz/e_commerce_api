from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import Category
from .serializers import CategorySerializer
from utils.response_json import CustomResponseJson

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return CustomResponseJson(statusCode=status.HTTP_200_OK, data=serializer.data).generate_success_json()
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponseJson(statusCode=status.HTTP_201_CREATED, data=serializer.data).generate_success_json()
        else:
            return CustomResponseJson(statusCode=status.HTTP_400_BAD_REQUEST, data={'error': 'Invalid data'}).generate_error_json()

class CategoryDetailView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return CustomResponseJson(statusCode=status.HTTP_200_OK, data=serializer.data).generate_success_json()
        except Category.DoesNotExist:
            return CustomResponseJson(statusCode=status.HTTP_404_NOT_FOUND, data={'error': 'Category not found'}).generate_error_json()
    
    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response({
                'status':'success',
                'message':'category has been deleted'
            }, status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return CustomResponseJson(statusCode=status.HTTP_404_NOT_FOUND, data={'error': 'Category not found'}).generate_error_json()
    
    def put(self, request, pk):
        try:    
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':'success',
                    'message':'data has been edited'
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'status':'error',
                    'message':'Invalid data'
                }, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return CustomResponseJson(statusCode=status.HTTP_404_NOT_FOUND, data={'error': 'Category not found'}).generate_error_json()
        

        
        
        
