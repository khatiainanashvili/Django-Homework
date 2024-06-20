from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from .models import Birds
# Create your views here.

def home(request):
    birds = Birds.objects.all()
    context = {"birds": birds}
    return render(request, 'myapp/home.html', context)

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, "myapp/contact.html")

