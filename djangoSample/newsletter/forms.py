from django import forms

from .models import SignUp

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ["full_name", "email"]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")
		# if not domain == "qburst":
		# 	raise forms.ValidationError("Please make sure you use the QBurst Email ID.")
		if not extension == "com":
			raise forms.ValidationError("Please make sure you use .com extension.")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get("full_name")
		# Write validation here
		return full_name
