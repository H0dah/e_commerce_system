from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=4, decimal_places=3)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"name: {self.name}, price: {self.price}"