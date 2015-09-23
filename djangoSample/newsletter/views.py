from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm, SignUpForm
# Create your views here.

def home(request):
	title = "Welcome"
	form = SignUpForm(request.POST or None)
	context = {
	    "title": title,
	    "form": form
	}

	if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get('full_name')
		if not full_name:
			full_name = 'Madhukar New Name'
		instance.full_name = full_name
		# if not instance.full_name:
		# 	instance.full_name = 'Madhukar'
		instance.save()
		context = {
			"title": "Thank you"
		}
	
	return render(request, 'home.html', context)


def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_full_name = form.cleaned_data.get("full_name")
		form_message = form.cleaned_data.get("message")
		form_email = form.cleaned_data.get("email")
		
		subject = "Site Contact Form"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'madhukar@qburst.com']
		full_name = form_full_name
		message = "have notified about your message"
		email = 'EMAIL'
		contact_message = "%s: %s via %s"%(
			full_name, 
			message, 
			email)

		send_mail(subject,
			contact_message,
			from_email,
			[to_email],
			fail_silently=False)

	context = {
		"form": form
	}

	return render(request, "forms.html", context)