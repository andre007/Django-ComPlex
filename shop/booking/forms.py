# coding=utf-8
from django import forms
from django.forms import ModelForm
from booking.models import Booking

class BookingForm(ModelForm):
    user_name = forms.CharField(
                max_length=30,
                error_messages={'required': 'Миннимум 10 символов'},
                widget=forms.TextInput(attrs={
                            'class':'form-control',
                        }))
    user_sec_name = forms.CharField(
                max_length=30,
                error_messages={'required': 'Миннимум 10 символов'},
                widget=forms.TextInput(attrs={
                            'class':'form-control',
                        }))
    user_mail = forms.EmailField()
    user_phone = forms.IntegerField()

    class Meta:
        model = Booking
        fields = ( "user_name", "user_sec_name", "user_mail", "user_phone")

