from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/', views.list, name='list'),
]