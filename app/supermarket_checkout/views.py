from .models import ShopingBasket as Basket, Product, Discount
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json

# Create your views here.
@csrf_exempt
def create_new_basket(request):
    if request.method != "POST":
        return HttpResponse(f"Wrong mehtod", status=400)
    basket = Basket.objects.create()
    return HttpResponse(json.dumps({"basket_id": basket.id}), status=201)


@csrf_exempt
def total_value_shopping_basket(request):
    if request.method != "GET":
        return HttpResponse(f"Wrong mehtod", status=400)
    basket_id = request.GET.get("basket_id")
    if basket_id is None:
        return HttpResponse(json.dumps({"error": "basket_id is required"}), status=400)
    
    basket = get_object_or_404(Basket, pk=basket_id)
    return HttpResponse(
        json.dumps({"total_value_shopping_basket": str(basket.current_total)}),
        status=200,
    )


@csrf_exempt
def add_product_to_basket(request):
    if request.method != "POST":
        return HttpResponse(f"Wrong mehtod", status=400)

    basket_id = request.POST.get("basket_id")
    product_id = request.POST.get("product_id")
    if basket_id is None or product_id is None:
        return HttpResponse(
            json.dumps({"error": "basket_id and product_id are required"}), status=400
        )
    quantity = int(request.POST.get("quantity", 1))
    quantity = quantity if quantity >= 1 else 1
    basket = get_object_or_404(Basket, pk=basket_id)
    product = get_object_or_404(Product, pk=product_id)

    basket.addItem(product, quantity)

    return HttpResponse(
        json.dumps({"current_total": str(basket.current_total)}), status=200
    )


@csrf_exempt
def basket_list_of_products(request):
    if request.method != "GET":
        return HttpResponse(f"Wrong mehtod", status=400)
    basket_id = request.GET.get("basket_id")
    basket = get_object_or_404(Basket, pk=basket_id)
    return HttpResponse(json.dumps(basket.products), status=200)
