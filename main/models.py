from django.db import models

class Categories(models.Model):
    title = models.CharField('Категория',max_length=255)
    logo = models.ImageField(upload_to='img/',default='Не выбрано')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Products(models.Model):
    title = models.CharField('Название', max_length=255)
    price = models.IntegerField('Цена')
    logo = models.ImageField(upload_to='img/')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    cat = models.CharField('Категория', max_length=255, default='Не выбрано')
    brand = models.CharField('Бренд', max_length=255, default='Не выбрано')
    color = models.CharField('Цвет', max_length=255, default='Не выбрано')
    display = models.CharField('Дисплей', max_length=255, default='Не выбрано')
    processor = models.CharField('Процессор', max_length=255, default='Не выбрано')
    ram = models.CharField('Оперативная память', max_length=255, default='Не выбрано')
    rom = models.CharField('Встроенная память', max_length=255, default='Не выбрано')
    camera = models.CharField('Камера', max_length=255, default='Не выбрано')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'