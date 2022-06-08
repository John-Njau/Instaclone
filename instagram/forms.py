from django import forms
from django.forms.widgets import TextInput, EmailInput, FileInput
from .models import Image, Profile, Comments


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
        
class CommentForm(forms.ModelForm):
    # text = forms.CharField(label='comment ...', max_length=100)
    
    class Meta:
        model = Comments
        fields = ('comment',)
        
        # widgets ={
        #     'comment': TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a comment'}),
        # }