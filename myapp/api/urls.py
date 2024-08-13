from django.urls import path # type: ignore
from . import views

urlpatterns = [

    path('', views.get_routes),
    path('birds/', views.get_birds),
    path('bird/<str:id>', views.get_bird),
]