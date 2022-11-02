from django import forms
from django.contrib.auth.forms import UserCreationForm
from signup.models import User

class UserForm(forms.ModelForm):
   class Meta:
     model = User
     fields = '__all__'

class UserCreationFormCustom(UserCreationForm):
  class Meta(UserCreationForm.Meta):
         fields = ['username','email','is_staff','password1','password2']

