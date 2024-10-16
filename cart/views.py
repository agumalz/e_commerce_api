from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import CartModel
from cart.serializers import CartSerializer
from utils.response_json import CustomResponseJson
from .forms import CartForm, LocationForm

class CartView(APIView):
    def get(self, request):
        cart = CartModel.objects.all()
        serializer = CartSerializer(cart, many=True)
        return CustomResponseJson(statusCode=status.HTTP_200_OK, data=serializer.data).generate_success_json()
    
    def post(self, request):
        form = CartForm(data=request.data)
        if form.is_valid():
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            
            try:
                cart, created = CartModel.objects.get_or_create(
                    product = product,
                    defaults={'quantity':quantity}
                )
                if not created:
                    cart.quantity += quantity
                    cart.save()
                serializer = CartSerializer(cart)
                return CustomResponseJson(statusCode=status.HTTP_201_CREATED, data=serializer.data).generate_success_json()
            except Exception as e:
                return CustomResponseJson(statusCode=status.HTTP_400_BAD_REQUEST, data={'error':str(e)}).generate_error_json() 
        else:
            return CustomResponseJson(statusCode=status.HTTP_400_BAD_REQUEST, data=form.errors).generate_error_json()
        
class CartDetailView(APIView):
    def delete(self, request, pk):
        try:
            cart = CartModel.objects.get(pk=pk)
            cart.delete()
            return CustomResponseJson(statusCode=status.HTTP_204_NO_CONTENT, data={'message':'Product deleted from the cart'}).generate_success_json()
        except CartModel.DoesNotExist:
            return CustomResponseJson(statusCode=status.HTTP_404_NOT_FOUND, data={'error':'Cart Not Found'}).generate_error_json()
        except Exception as e:
            return CustomResponseJson(statusCode=status.HTTP_400_BAD_REQUEST, data={'error':str(e)}).generate_error_json()

class CartQuantityIncrease(APIView):
    def put(self, request, pk):
        try:
            cart = CartModel.objects.get(pk=pk)
            cart.quantity += 1
            cart.save()
            
            serializer = CartSerializer(cart)
            return CustomResponseJson(statusCode=status.HTTP_200_OK, data=serializer.data).generate_success_json()
        except CartModel.DoesNotExist:
            return CustomResponseJson(statusCode=status.HTTP_404_NOT_FOUND, data={'error':'Cart Not Found'}).generate_error_json()
        except Exception as e:
            return CustomResponseJson(statusCode=status.HTTP_400_BAD_REQUEST, data={'error':str(e)}).generate_error_json()

class CartQuantityDecrease(APIView):
    def put(self, request, pk):
        try:
            cart = CartModel.objects.get(pk=pk)
            
            if cart.quantity > 1:
                cart.quantity -= 1
                cart.save()
            
            serializer = CartSerializer(cart)
            return CustomResponseJson(statusCode=status.HTTP_200_OK, data=serializer.data).generate_success_json()
        except CartModel.DoesNotExist:
            return CustomResponseJson(statusCode=status.HTTP_404_NOT_FOUND, data={'error':'Cart Not Found'}).generate_error_json()
        except Exception as e:
            return CustomResponseJson(statusCode=status.HTTP_400_BAD_REQUEST, data={'error':str(e)}).generate_error_json()


class CheckOut(APIView):
    def post(self, request):
        form = LocationForm(data=request.data)
        if form.is_valid():
            cart_items = CartModel.objects.all()
            cart_serializer = CartSerializer(cart_items, many=True)
            
            total_weight = sum(item['product_weight'] for item in cart_serializer.data)
            total_price = sum(item['price'] for item in cart_serializer.data)
            
            api_key = "36e7a7e86fb50a3e4c60140d0a35bb8a"
            
            origin = form.cleaned_data['origin']
            destination = form.cleaned_data['destination']
            response_data = {'products': [], 'total_weight': total_weight, 'total_price': total_price}
            
            # Calculate shipping cost
            shipping_cost = self.calculate_shipping_cost(api_key, origin, destination, total_weight, 'jne')
            if shipping_cost is None:
                return Response({"error": "Failed to calculate shipping cost"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            total_overall = total_price + shipping_cost
            
            # Prepare product information
            for item in cart_serializer.data:
                product_info = {'product': item['product']['name'], 'quantity': item['quantity']}
                response_data['products'].append(product_info)
            
            # Delete cart items after successful checkout
            # cart_items.delete()
            
            # Update response data with shipping cost and total overall
            response_data.update({'shipping_cost': shipping_cost, 'total_overall': total_overall})
            
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def calculate_shipping_cost(self, api_key, origin, destination, weight, courier):
        url = 'https://api.rajaongkir.com/starter/cost'
        
        payload = {
            'key': api_key, 
            'origin': origin,
            'destination': destination,
            'weight': weight,
            'courier': courier
        }
        
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            results = response.json().get('rajaongkir', {}).get('results', [])
            if results:
                shipping_cost = results[0]['costs'][1]['cost'][0]['value']
                return shipping_cost
        return None  # Return None if shipping cost calculation fails

