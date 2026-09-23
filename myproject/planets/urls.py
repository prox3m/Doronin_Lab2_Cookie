from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('planet/<slug:slug>/', views.planet_detail, name='planet_detail'),
]