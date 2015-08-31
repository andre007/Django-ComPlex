# coding=utf-8
from django import forms
from django.forms import ModelForm
from contact.models import Feedback

class FeedBackForm(ModelForm):
    name = forms.CharField(max_length=50,
                error_messages={'required': 'Миннимум 10 символов'},
                widget=forms.TextInput(attrs={
                            'class':'form-control',
                        }))
    feedback_email = forms.EmailField()
    company = forms.CharField(max_length=50,
                error_messages={'required': 'Миннимум 10 символов'},
                widget=forms.TextInput(attrs={
                            'class':'form-control',
                        }))
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Feedback
        fields = ("name", "feedback_email", "company", "message")
