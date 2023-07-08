from django.db import models

#Класс Model из пакета models позволяет из
#обычного python класса сделать модель(таблицу для БД)

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

