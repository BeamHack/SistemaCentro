from models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserCreationEmailForm(UserCreationForm):
	email=forms.EmailField()
	class Meta:
		model=User
		fields=('username','email')


class EmailAuthenticationForm(forms.Form):
	email=forms.EmailField()
	password=forms.CharField(label='contrasena', widget=forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		self.user_cache=None
		super(EmailAuthenticationForm, self).__init__(*args, **kwargs)

	def clean(self):
		email=self.cleaned_data.get('email')
		password=self.cleaned_data.get('password')

		self.user_cache=authenticate(email=email, password=password)

		if self.user_cache is None:
			raise forms.ValidationError('Usuario Incorrecto')
		elif not self.user_cache.is_active:
			raise forms.ValidationError('Usuario Inactivo')

		return self.cleaned_data


	def get_user(self):
		return self.user_cache




