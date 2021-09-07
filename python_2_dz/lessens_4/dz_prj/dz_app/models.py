from django.db import models


class Prodacts_info(models.Model):
    title = models.CharField(
        verbose_name='Название', 
        max_length=50
    )

    created_at = models.DateTimeField(
        verbose_name='Дата доставки' 
    )

    price = models.PositiveIntegerField(
        verbose_name='Цена', 
        default=0
    )

    count = models.PositiveIntegerField(
        verbose_name='Колличество на складе', 
        default=0
    )

    vendor = models.CharField(
        verbose_name='Поставщик',
        max_length=100
    )

