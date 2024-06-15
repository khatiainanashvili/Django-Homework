from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact)
]
