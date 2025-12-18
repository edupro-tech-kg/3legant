from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name = 'Название')
    description = models.TextField(verbose_name = 'Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name = 'Цена')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name = 'Изображение')
    in_stock = models.BooleanField(default=True, verbose_name = 'В наличии')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Создан')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
                                 null=True, related_name= 'products', verbose_name = 'Категория')
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL,
                                 null=True, related_name='products', verbose_name='Бренд')


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ("-created_at", )

    def __str__(self):
        return f'{self.title} - {self.price}'

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Brand(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'





