from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index_view(request):
    # return HttpResponse("<h1> Home Page !</h1>")

    return render(request, 'website/index.html')

def contact_view(request):
    # return HttpResponse("<h1> Contact Page !</h1>")

    return render(request, 'website/contact.html')

def about_view(request):
    # return HttpResponse("<h1> About Page !</h1>")

    return render(request, 'website/about.html')

def http_test(request):
    return HttpResponse("<h1>hello World !</h1>")

def json_test(request):
    return JsonResponse({"name" : "Hossein"})