from django.urls import path
from .views import ProvinceAPIView

urlpatterns = [
    path('', ProvinceAPIView.as_view(), name='province')
]


