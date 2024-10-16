from django.urls import path
from category.views import CategoryListView, CategoryDetailView

urlpatterns = [
    path('list/', CategoryListView.as_view(), name='list'),
    path('detail/<int:pk>/', CategoryDetailView.as_view(), name='detail'),
]