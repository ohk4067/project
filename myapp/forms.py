from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from datetime import datetime

class SignUpForm(UserCreationForm):
    nowdate = datetime.now()
    # today = nowdate.strftime("%y%m%d")
    last_login = forms.DateTimeField(initial=nowdate, widget=forms.HiddenInput)
    date_joined = forms.DateTimeField(initial=nowdate, widget=forms.HiddenInput)
    is_superuser = forms.BooleanField(widget=forms.HiddenInput)
    is_staff = forms.BooleanField(widget=forms.HiddenInput)
    is_active = forms.BooleanField(widget=forms.HiddenInput)

    class Meta:
        model = User
        fields = ('id','last_login','is_superuser','username','first_name', 'last_name','email','is_staff','is_active','date_joined')

# class PostForm(forms.Post):
#     nowdate = datetime.now()
#     user = forms.CharField(widget=forms.HiddenInput)
#     title = forms.CharField(widget=forms.HiddenInput)s
#     message = forms.CharField(widget=forms.HiddenInput)
#     image = forms.ImageField(widget=forms.HiddenInput)
#     date = forms.DateField(initial=nowdate,widget=forms.HiddenInput)
#     writer = forms.CharField(widget=forms.HiddenInput)
#     class Meta:
#         model = Post
#         fields = ('user','title','message','image','date', 'writer')

