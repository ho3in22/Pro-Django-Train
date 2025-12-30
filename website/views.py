from django.http import HttpResponse, JsonResponse


def index_view(request):
    return HttpResponse("<h1> Home Page !</h1>")

def contact_view(request):
    return HttpResponse("<h1> Contact Page !</h1>")

def about_view(request):
    return HttpResponse("<h1> About Page !</h1>")

def http_test(request):
    return HttpResponse("<h1>hello World !</h1>")

def json_test(request):
    return JsonResponse({"name" : "Hossein"})