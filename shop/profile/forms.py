# coding: utf-8
# author: dlyapun

from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from profile.models import CustomUser


class UserCreateForm(UserCreationForm):
    username = forms.CharField(
                max_length=30,
                error_messages={'required': 'Миннимум 10 символов'},
                widget=forms.TextInput(attrs={
                            'class':'form-control',
                        }))
    email = forms.EmailField(
                widget=forms.TextInput(attrs={
                            'placeholder':'example@mail.com',
                            'class':'form-control'
                        }))
    first_name = forms.CharField(
                max_length=30,
                widget=forms.TextInput(attrs={
                            'placeholder':'Антон',
                            'class':'form-control',
                        }))
    last_name = forms.CharField(
                max_length=30,
                widget=forms.TextInput(attrs={
                            'placeholder':'Иванов',
                            'class':'form-control',
                        }))
    company_name = forms.CharField(max_length=150, widget = forms.TextInput(attrs={'placeholder':'Название компании','class':'form-control',}))

    phone = forms.CharField(max_length=20, widget =  forms.TextInput(attrs={'placeholder':'0000000','class':'form-control',}))

    password1 = forms.CharField(
                max_length=30,
                widget=forms.PasswordInput(attrs={
                            'class':'form-control',
                        }))
    password2 = forms.CharField(
                max_length=30,
                widget=forms.PasswordInput(attrs={
                            'class':'form-control',
                        }))

    class Meta:
        model = User
        fields = ("username", "email", "company_name", "password1", "password2")


    #def custom_user_save(self, user, company_name):
    #    custom_user = CustomUser.objects.get(user=user)
    #    print(company_name)
    #    custom_user.company_name = self.cleaned_data["company_name"]
    #    print(company_name +"Hui")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        #user.company_name = self.cleaned_data["company_name"]
        #custom_user = CustomUser.objects.get(user=user)
        #custom_user.company_name = self.cleaned_data["company_name"]
        form_company_name = self.cleaned_data["company_name"]
        form_phone = self.cleaned_data["phone"]


        if commit:
            user.save()
            p = CustomUser.objects.create(user=user)
        #self.custom_user_save(user, company_name)
        custom_user = CustomUser.objects.get(user=user)
        custom_user.company_name = form_company_name
        custom_user.phone=form_phone
        custom_user.email=user.email
        custom_user.first_name=user.first_name
        custom_user.last_name=user.last_name
        custom_user.save()
        return user





class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
                max_length=30,
                error_messages={'required': 'Миннимум 10 символов'},
                widget=forms.TextInput(attrs={
                            'class':'form-control',
                        }))

    password = forms.CharField(
                max_length=30,
                widget=forms.PasswordInput(attrs={
                            'class':'form-control',
                        }))


class CustomUserForm(ModelForm):
    first_name = forms.CharField(
                max_length=30,
                widget=forms.TextInput(attrs={
                            'placeholder':'Антон',
                            'class':'form-control',
                        }))
    last_name = forms.CharField(
                max_length=30,
                widget=forms.TextInput(attrs={
                            'placeholder':'Иванов',
                            'class':'form-control',
                        }))

    about = forms.CharField(
                max_length=500,
                required=False,
                widget=forms.Textarea(attrs={
                            'placeholder':'Пару слов про себя',
                            'class':'form-control',
                        }))
    status = forms.CharField(
                max_length=50,
                required=False,
                widget=forms.TextInput(attrs={
                            'placeholder':'Статус',
                            'class':'form-control',
                        }))
    phone = forms.CharField(
                max_length=20,
                required=False,
                widget=forms.TextInput(attrs={
                            'placeholder':'Телефон',
                            'class':'form-control',
                        }))
    vk = forms.URLField(
                max_length=50,
                required=False,
                widget=forms.TextInput(attrs={
                            'placeholder':'Вконтакте',
                            'class':'form-control',
                        }))
    facebook = forms.URLField(
                max_length=50,
                required=False,
                widget=forms.TextInput(attrs={
                            'placeholder':'Facebook',
                            'class':'form-control',
                        }))
    od_class = forms.URLField(
                max_length=50,
                required=False,
                widget=forms.TextInput(attrs={
                            'placeholder':'Одноклассники',
                            'class':'form-control',
                        }))
    date_of_birth = forms.DateField(
                required=False,
                widget=forms.TextInput(attrs={
                            'placeholder':'Дата Рождения',
                            'class':'form-control',
                        }))

    class Meta:
        model = CustomUser
        exclude = ['user', 'karma', 'writer', 'valid_member', 'moderator', 'goverment', 'instructor',]

    def save(self, *args, **kw):
        super(CustomUserForm, self).save(*args, **kw)
        self.instance.user.first_name = self.cleaned_data.get('first_name')
        self.instance.user.last_name = self.cleaned_data.get('last_name')
        self.instance.user.save()