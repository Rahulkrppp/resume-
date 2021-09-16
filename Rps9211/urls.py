from django.urls import path
from Rps9211 import views

urlpatterns = [
    path('',views.Login,name='login'),
    path('home',views.home,name='home') 
]
