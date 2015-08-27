# coding=utf-8

from django.db import models


class Product(models.Model):
    DISABLE = 0
    ENABLE = 1
    HOT_NEW = 2

    STATE_CHOICE = (
        (DISABLE, 'Disable'),
        (ENABLE, 'Enable'),
        (HOT_NEW, 'Hot New'),
    )

    name = models.CharField(max_length=50, verbose_name="Продукт")
    full_text = models.TextField()
    short_text = models.TextField()
    price = models.IntegerField()
    date_creation = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Categories')
    mainphoto =  models.ImageField(upload_to='PhotoImage/',
                                     verbose_name=u'ГлавФото')
    photos = models.ManyToManyField('Photo',
                                    blank=True, null=True)
    miniphotos = models.ManyToManyField('Miniphoto', blank = True, null = True)
    state = models.SmallIntegerField(default=ENABLE,
                                     choices=STATE_CHOICE,
                                     verbose_name=u'Статус')

    class Meta:
        ordering = ["-date_creation"]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return u'/party/%s' % self.id
    

class Categories(models.Model):
    categories = models.CharField(max_length=150, 
                                  verbose_name=u'Категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return u'/product_list/%s' % self.id

    def __unicode__(self):
        return self.categories




class Photo(models.Model):
    photography =  models.ImageField(upload_to='Image/',
                                     verbose_name=u'Фотография')
    photo_description = models.CharField(max_length=50, 
                                         verbose_name=u'Описание фотографии')



class Miniphoto(models.Model):
    miniphoto =  models.ImageField(upload_to='MiniPhotoImage/',
                                     verbose_name=u'Фотография')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
