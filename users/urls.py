from django.urls import path
from .views import *

urlpatterns = [
    path('login/', userLogin),
    path('logout/', LogoutView.as_view()),
    path('register/',userRegister),
    path('refresh/',refresh.as_view())
]