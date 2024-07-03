from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/<str:id>/', views.profile, name='profile'),
    path('adding/<str:id>/', views.adding, name='adding'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),

]
