import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'tag','thumbnail_image', 'feature_image')

class CommentForm(forms.ModelForm):
     class Meta:
         model = Comments
         fields = ('name', 'email', 'comment')

class CategoryForm(forms.ModelForm): 
    class Meta:
        model = Category
        fields = ('name',)

class LoginForm(forms.Form): 
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)   


class SignUpForm(UserCreationForm):  
     class Meta:
         model = MyUser
         fields = ('username','email','mobileNumber','city', 'country', 'company','gender',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model =  MyUser
        fields = ('username','first_name', 'last_name','image', 'email','mobileNumber', 'country', 'city')