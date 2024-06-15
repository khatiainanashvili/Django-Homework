from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, "contact.html")

