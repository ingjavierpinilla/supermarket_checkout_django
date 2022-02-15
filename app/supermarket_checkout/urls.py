from django.urls import path
from .views import (
    create_basket,
    total_value_shopping_basket,
    add_product_to_basket,
    basket_list_of_products,
)

urlpatterns = [
    path("v1/create-basket", create_basket),
    path("v1/total-value-shopping-basket", total_value_shopping_basket),
    path("v1/add-product-to-basket", add_product_to_basket),
    path("v1/basket-list-of-products", basket_list_of_products),
]
