from django.urls import path
from . import views
from .views import product_detail, add_product

urlpatterns = [
    path("", views.home, name="home"),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('add-product/', add_product, name='add_product'),
]
