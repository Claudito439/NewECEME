from django.urls import path
from .views import *

urlpatterns = [
    path('menu/', MenuListView),
    path('buscar/', BuscarView),
]