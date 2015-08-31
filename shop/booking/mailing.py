# coding=utf-8
from django.template.loader import render_to_string



def email_message(user_name, user_sec_name, user_mail, user_phone, total_price):
	message = render_to_string('message.txt', {
	'user_name': user_name,
	'user_sec_name': user_sec_name,
	'user_mail': user_mail,
	'user_phone': user_phone,
	'total_price': total_price,
	})
	return message

def feeback_email(name, feedback_email, company, message):
	feedback = render_to_string('feedback.txt', {
	'name': name,
	'feedback_email': feedback_email,
	'company': company,
	'message': message,
	})
	return feedback