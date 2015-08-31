# coding=utf-8

from django.contrib.auth.models import User, UserManager
from django.db import models
from django.conf import settings


class CustomUser(models.Model):
    user = models.OneToOneField("auth.User")
    phone = models.CharField(max_length=30, 
                             verbose_name=u'Номер', 
                             blank=True, null=True)

    company_name = models.CharField(max_length=150, verbose_name=u'Название компании', blank=False)
    #moderator = models.BooleanField(default=False, verbose_name=u'Модератор') 
    confirmed = models.BooleanField(default=False, verbose_name=u'Подтвержден')

    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    objects = UserManager() 

    def get_absolute_url(self):
        return u'/profile/%s' % self.id

    def get_full_name(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)

    def __unicode__(self):
        return self.user.username


