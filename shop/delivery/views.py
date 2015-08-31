# coding=utf-8
from django.shortcuts import render
from delivery.models import InfoColumn, FAQ 

# Create your views here.
def delivery(request):
	columns = InfoColumn.objects.filter(state=1)[:3]
	faqs = FAQ.objects.all()
	data = {'columns':columns, 'faqs':faqs}
	return render(request, 'delivery.html', data)