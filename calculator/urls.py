from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("calc", views.calc),
    path("regiser/", views.register, name="regiser"),    
]