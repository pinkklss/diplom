from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)  # имя
    description = models.TextField()         # описание
    price = models.DecimalField(max_digits=10, decimal_places=2)  # цена
    quantity_in_stock = models.IntegerField()  # кол-во

