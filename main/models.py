from django.db import models
from django.contrib.auth.models import User

class Req(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    GENDER_CHOICES = [
        ('male', 'Самец'),
        ('female', 'Самка'),
    ]
    STATUS_CHOICES = [
        ('approved', 'Одобрена'),
        ('rejected', 'Не одобрена'),
    ]

    name = models.CharField(max_length=150, verbose_name='Имя')
    gen = models.CharField(max_length=150, verbose_name='Порода')
    sex = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name='Пол', blank=True, null=True)
    color = models.CharField(max_length=150, verbose_name='Цвет')
    desc = models.TextField(verbose_name='Дополнительная атрибутика')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='approved', verbose_name='Статус заявки')
