from django import forms
from django.forms import *
from blog.models import *
from captcha.fields import CaptchaField

class CommentForm(ModelForm):
    # captcha = CaptchaField()
    class Meta:
        model = Comment
        fields = ['post','name','email','subject','message']
