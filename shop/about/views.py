# coding=utf-8
from django.shortcuts import render
from about.models import About


# Create your views here.
def about(request):
    #about = About.objects.filter(state=1)
    try:
        about = About.objects.get(state=1)
    except About.DoesNotExist:
        about = None
    data = {'about':about}
    return render(request, 'about.html', data)