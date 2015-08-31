# coding=utf-8
from django.db import models

# Create your models here.
class About(models.Model):
    DISABLE = 0
    ENABLE = 1

    STATE_CHOICE = (
        (DISABLE, 'Disable'),
        (ENABLE, 'Enable'),
    )
    about_text = models.TextField(verbose_name="О нас")
    state = models.SmallIntegerField(default=ENABLE,
    								choices=STATE_CHOICE,
                                    verbose_name=u'Статус')