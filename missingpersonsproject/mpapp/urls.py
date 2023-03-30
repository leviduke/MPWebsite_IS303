#Levi Duke

#This file determines the routes of where the user will go
from .views import indexPageView
from django.urls import path


urlpatterns = [
    path("",indexPageView, name="index")
]
