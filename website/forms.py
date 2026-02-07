from django import forms
from django.forms import *
from website.models import *

# class ContactForm(Form):
#     name = CharField(max_length=255)
#     email = EmailField()
#     subject = CharField(max_length=255)
#     message = CharField(widget=forms.Textarea)

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        # fields = ['name', 'email']
        # exclude = ['name']

class NewsLetterForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'