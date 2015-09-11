from contact.models import CompanyInfo

def context_contact(request):
	try:
		companyinfo = CompanyInfo.objects.get()
	except CompanyInfo.DoesNotExist:
		companyinfo = None
	return{'companyinfo': companyinfo}