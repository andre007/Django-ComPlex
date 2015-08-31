# coding=utf-8
from django.db import models
from cart.models import Cart, Item
# Create your models here.
class Mail(models.Model):
	delivery_mail = models.EmailField(verbose_name="Почта")


class Booking(models.Model):
	name = models.CharField(max_length=50, verbose_name="Заказ")
	#cart_name = models.ManyToManyField('Cart')
	items = models.ManyToManyField('Item', null=True)
	total_sum = models.IntegerField(max_length=50, verbose_name="Сумма", null=True)
	user_name = models.CharField(max_length=50, verbose_name="Имя пользователя", null=True)
	user_sec_name = models.CharField(max_length=50, verbose_name="Фамилия", null=True)
	user_mail = models.EmailField(max_length=50, verbose_name="Почта пользователя", null=True)
	user_phone = models.IntegerField(max_length=50, verbose_name="Контактный телефон", null=True)


