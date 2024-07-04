from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from .models import Birds, User, Country
from django.db.models import Q # type: ignore
from django.contrib.auth import authenticate, login, logout# type: ignore
# Create your views here.

def home(request):
    query = request.GET.get('query', "")
    # birds = Birds.objects.all()
    birds = Birds.objects.filter(Q(species__icontains=query) | Q(descroption__icontains=query))
    headline = "Rare Birds"
    context = {"birds": birds, "headline": headline}
    return render(request, 'myapp/home.html', context)

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, "myapp/contact.html")

def profile(request, id):
    user = User.objects.get(id=int(id))
    query = request.GET.get('query', "")
    birds = user.birds.filter(Q(species__icontains=query) | Q(descroption__icontains=query))
    # birds = user.birds.all()

    headline= "My Favorite Birds"
    context = {"birds": birds, "user": user, "headline": headline}
    return render(request, "myapp/profile.html", context)

def adding(request, id):
    bird = Birds.objects.get(id=id)
    user = request.user
    user.birds.add(bird)
    print(id)
    return redirect('profile', user.id)

def delete(request, id):
    bird = Birds.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        request.user.birds.remove(bird)
        return redirect('profile', user.id)
    return render(request, "myapp/delete.html", {'bird': bird})


def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return render('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            pass

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            pass
        


    context = {'page': page}
    return render(request, 'myapp/login-register.html', context)

def log_out(request):
    logout(request)
    return redirect('home')


def register_page(request):
    page = ''
    context = {}
    return render(request, 'myapp/login-register.html', context)


