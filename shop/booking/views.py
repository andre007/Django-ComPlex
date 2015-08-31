# coding=utf-8
from django.shortcuts import render
#from cart import Cart
from booking.models import Mail, Booking
from cart.models import Item, Cart
from booking.forms import BookingForm
from django.http import Http404, HttpResponseRedirect
from django.core.mail import send_mail
from booking.mailing import email_message
from profile.models import CustomUser
# Create your views here.

def thanx(request):
    return render(request, 'thanx.html', {'no_data':0})

def booking(request):
    #THIS IS COSTYL
    cart_list = Cart.objects.all()
    CART_ID='CART-ID'
    cart_id=request.session[CART_ID]
    print(request.session[CART_ID])
    user_cart = Cart.objects.get(id=cart_id)
    item_list = Item.objects.filter(cart = user_cart)
    mailing_list = Mail.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            #form.save()
            i = 1
            total_price = 0
            for item in item_list:
                total_price += item.product.price
            user_name = form.cleaned_data['user_name']
            user_sec_name = form.cleaned_data['user_sec_name']
            user_mail = form.cleaned_data['user_mail']
            user_phone =form.cleaned_data['user_phone']
            booking_item = Booking(name = "Заказ номер" + " " + str(i), user_name = user_name, user_sec_name=user_sec_name, user_mail=user_mail, user_phone = user_phone, total_sum=total_price)
            booking_item.save()
            message = email_message(user_name, user_sec_name, user_mail, user_phone, total_price)
            print(item_list)
            for item in item_list:
                booking_item.items.add(item)
            i+=1
        return HttpResponseRedirect("/thanx/")
    else:
        form = BookingForm()
    data = {'form': form}

    return render(request, 'bookings.html', data)


def registered_booking(request):
    user_cart = Cart.objects.all()
    item_list = Item.objects.filter(cart = user_cart)
    mailing_list = Mail.objects.all()
    total_price=0
    if request.user.is_authenticated():
        user=request.user
        custom_user = CustomUser.objects.get(user=user)
        for item in item_list:
            total_price += item.product.price
        #Unblock on production
        #discount_total_price = total_price*(custom_user.discount/100)
        discount_total_price = total_price*0.2
        booking_item = Booking(name = "Заказ номер" + " " + str(1), user_name = user. first_name, user_sec_name=user.last_name, user_mail=user.email, user_phone = custom_user.phone, total_sum=discount_total_price)
        booking_item.save()
        for item in item_list:
                booking_item.items.add(item)
        return HttpResponseRedirect("/thanx/")