from django.urls import path
from FruitipediaApp.fruits import views

urlpatterns = [
    path('', views.index, name='index'),
]