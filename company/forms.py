from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(ModelForm):

    class Meta:
        model = User
        fields =('email',)

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password',)


class AddPeopleForm(ModelForm):
    class Meta:
        model = User
        fields = ('name','email','type')

class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('name','phone','gender','hobbies','profile_picture')
