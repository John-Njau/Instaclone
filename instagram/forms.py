from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import TextInput, EmailInput, FileInput

from .models import Image, Profile, User

class SignUpForm(UserCreationForm):
    class Meta:
       model = User
       fields = ('username', 'email', 'password1', 'password2')
       
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
       
class LoginForm(forms.Form):
    username = forms.CharField( max_length=30)
    password = forms.PasswordInput()
    
    class Meta:
        fields = ('username', 'password')
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image','caption']
        
        widgets ={
            'image': FileInput(attrs={'class': 'form-control'}),
            'caption': TextInput(attrs={'class': 'form-control', 'placeholder': 'write something'}),
        }
        

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profilepic', 'bio']
        
        widgets ={
            'profilepic': FileInput(attrs={'class': 'form-control'}),
            'bio': TextInput(attrs={'class': 'form-control', 'placeholder': 'Update Bio'}),
        }