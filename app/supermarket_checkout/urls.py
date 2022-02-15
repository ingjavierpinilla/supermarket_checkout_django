from django.urls import path
from .views import (
    create_new_basket,
    total_value_shopping_basket,
    add_product_to_basket,
    basket_list_of_products,
)

urlpatterns = [
    path("v1/create_new_basket", create_new_basket),
    path("v1/total_value_shopping_basket", total_value_shopping_basket),
    path("v1/add_product_to_basket", add_product_to_basket),
    path("v1/basket_list_of_products", basket_list_of_products),
]
