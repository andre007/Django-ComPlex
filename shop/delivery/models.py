# coding=utf-8
from django.db import models

# Create your models here.
class InfoColumn(models.Model):
    DISABLE = 0
    ENABLE = 1

    STATE_CHOICE = (
        (DISABLE, 'Disable'),
        (ENABLE, 'Enable'),
    )
    column_text = models.TextField(verbose_name='Колонка')
    state = models.SmallIntegerField(default=DISABLE, choices=STATE_CHOICE)
    photo = models.ImageField(verbose_name='Изображение', upload_to='Delivery')
    header = models.CharField(max_length=50, verbose_name='Заглавие')

class FAQ(models.Model):
    question = models.CharField(max_length=150, verbose_name='Вопрос')
    answer = models.CharField(max_length=150, verbose_name='Ответ')