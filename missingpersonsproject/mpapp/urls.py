#Levi Duke

#This file determines the routes of where the user will go
from .views import indexPageView
from django.urls import path
<<<<<<< HEAD
from .views import individualpersonPageView
from .views import missingpersonstablePageView


urlpatterns = [
    path("",indexPageView, name="index"),
    path("mptable/", missingpersonstablePageView, name="mptable"  ),
    path("individualperson/", individualpersonPageView, name = "individualperson"),
=======


urlpatterns = [
    path("",indexPageView, name="index")
>>>>>>> origin/master
]
