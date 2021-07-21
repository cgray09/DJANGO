from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django import forms
from .models import Order

class CreateUserForm(UserCreationForm):
	# meta to extend the features of the django form
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = "__all__" #gives us all of the fields from Order