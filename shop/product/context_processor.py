#context_processor.py
from product.models import Product

def context_profile(request):
	new_prods = Product.objects.filter(state=HOT_NEW)[:4]
	return {'new_prods': new_prods}