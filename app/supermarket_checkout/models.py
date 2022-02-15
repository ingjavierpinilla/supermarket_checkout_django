from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from picklefield.fields import PickledObjectField

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, default="")
    price = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=6,
        validators=[MinValueValidator(0)],
    )

    def __str__(self):
        return f"{self.id}, {self.name} ${self.price}"


class ShopingBasket(models.Model):
    products = PickledObjectField(default=dict)
    current_total = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=6,
        validators=[MinValueValidator(0)],
    )

    def addItem(self, product_to_add, quantity):
        product_dict = self.products.get(product_to_add.id, None)
        discount = Discount.objects.get(product=product_to_add)

        if product_dict is None:
            self.products[product_to_add.id] = {
                "name": product_to_add.name,
                "quantity": quantity,
            }
        else:
            self.products[product_to_add.id]["quantity"] += quantity

        if quantity / discount.quantity >= 1:
            offers_to_apply = int(
                quantity / discount.quantity
                if quantity % discount.quantity == 0
                else quantity % discount.quantity
            )
            self.current_total += discount.new_price * offers_to_apply
            quantity -= offers_to_apply * discount.quantity
            self.save()
        if quantity > 0:
            self.current_total += product_to_add.price * quantity
        self.save()


class Discount(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.BigIntegerField(default=1, validators=[MinValueValidator(0)])
    new_price = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=6,
        validators=[MinValueValidator(0)],
    )

    def __str__(self):
        return f"{self.product}, {self.quantity} for {self.new_price}"
