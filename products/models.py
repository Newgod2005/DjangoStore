from django.db import models

#Класс Model из пакета models позволяет из
#обычного python класса сделать модель(таблицу для БД)

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    #Цифры до запятой и после запятой. DecimalField - тип данных для цены
    quantity =models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)