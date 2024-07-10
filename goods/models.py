from django.db import models

class Popug(models.Model):
    GENDER_CHOICES = [
        ('male', 'Самец'),
        ('female', 'Самка'),
    ]


    name = models.CharField(max_length = 150, unique = True, verbose_name = 'Название')
    gen = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name = 'Пол', blank = True, null= True)
    desc = models.TextField(verbose_name = 'Описание')
    image = models.ImageField(upload_to='goods_images',blank = True, null = True, verbose_name = 'Изображение' )
    price = models.DecimalField(default = 0.00, max_digits = 7, decimal_places = 2,verbose_name = 'Цена')

    class Meta:
        db_table = 'popug'
        verbose_name = 'Попугай'
        verbose_name_plural = 'Попугаи'



from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goods = models.ManyToManyField('Popug')

    def __str__(self):
        return f"Cart for {self.user.username}"
