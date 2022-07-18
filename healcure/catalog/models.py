from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'

    name = models.CharField(max_length=15, verbose_name='Название')

    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'

    name = models.CharField(max_length=80, verbose_name='Название')
    article = models.PositiveSmallIntegerField(verbose_name='Артикль', null=True)
    brand = models.CharField(max_length=15,verbose_name='Брэнд')
    main_desc = models.TextField(verbose_name='Описание', null=True)
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null=True, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена', null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog-detail', args=[str(self.id)])




