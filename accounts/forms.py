from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		
		model = User
		fields = UserCreationForm.Meta.fields 