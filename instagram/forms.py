from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import TextInput, EmailInput

from .models import User, Subscriber

class SignUpForm(UserCreationForm):
    class Meta:
       model = User
       fields = ('username', 'email', 'password1', 'password2')
       
       
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)
        
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'johndoe@ymail.com', 'id': 'email'}),
        }
        

class LoginForm(forms.Form):
    username = forms.CharField(label='usernameme', max_length=30)
    password = forms.PasswordInput(label='Password')
    
    class Meta:
        fields = ['username', 'password']