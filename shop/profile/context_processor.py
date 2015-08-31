#context_processor.py
from profile.models import CustomUser
#from django.contrib.auth.models import User

def context_profile(request):
	not_open = 0
	if request.user.is_authenticated():
		if request.user.is_superuser:
			return {"not_to_open_this_sheet_ever":not_open}
		else:
			user = request.user
			custom_user = CustomUser.objects.get(user=user)
			return {"custom_user": custom_user}
	else:
		return {"not_to_open_this_sheet_ever":not_open}