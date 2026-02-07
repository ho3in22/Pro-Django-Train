from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.forms import *
from website.models import *
from django.contrib import messages


def index_view(request):
    # return HttpResponse("<h1> Home Page !</h1>")

    return render(request, 'website/index.html')

def contact_view(request):
    # return HttpResponse("<h1> Contact Page !</h1>")
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # subject = form.cleaned_data['subject']
            # message = form.cleaned_data['message']
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your email added !')
        else :
            messages.add_message(request, messages.ERROR, 'Your email DID NOT added !')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/')

def about_view(request):
    # return HttpResponse("<h1> About Page !</h1>")

    return render(request, 'website/about.html')

def http_test(request):
    return HttpResponse("<h1>hello World !</h1>")

def json_test(request):
    return JsonResponse({"name" : "Hossein"})