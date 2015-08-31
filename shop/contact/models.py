# coding=utf-8
from django.db import models

# Create your models here.
class Feedback(models.Model):
	name = models.CharField(max_length=50, verbose_name="имя")
	feedback_email = models.EmailField()
	company = models.CharField(max_length=50, verbose_name="Компания")
	message = models.TextField()

class CompanyInfo(models.Model):
	name = models.CharField(max_length=50, verbose_name="имя компании")
	adress = models.CharField(max_length=150, verbose_name="Адресс")
	country = models.CharField(max_length=20)
	phone = models.IntegerField()
	company_email = models.EmailField()