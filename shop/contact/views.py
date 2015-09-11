# coding=utf-8
from django.shortcuts import render
from contact.models import CompanyInfo
from contact.forms import FeedBackForm
from booking.models import Mail
from booking.mailing import feeback_email
from django.http import Http404, HttpResponseRedirect

# Create your views here.
def thanx(request):
	return render(request, 'feedback_thanx.html', {'no_data':0})

def contact(request):
	try:
		companyinfo = CompanyInfo.objects.get()
	except CompanyInfo.DoesNotExist:
		companyinfo = None
	if request.method == 'POST':
		form = FeedBackForm(request.POST, request.FILES)
		if form.is_valid():
			name=form.cleaned_data['name']
			feedback_email=form.cleaned_data['feedback_email']
			company=form.cleaned_data['company']
			message=form.cleaned_data['message']
			form.save()
			feedback_message = feeback_email(name, feedback_email, company, message)
			#UNBLOCK ON PRODUCTION
            #send_mail('Прислан коментарий', feedback_message, 'amax9x@gmail.com',
            #mailing_list, fail_silently=False)
			return HttpResponseRedirect("/feedback_thanx/")
	else:
		form = FeedBackForm()
    	data = {'form': form, 'companyinfo':companyinfo}
    	#print(companyinfo.name)

    	return render(request, 'contact.html', data)
