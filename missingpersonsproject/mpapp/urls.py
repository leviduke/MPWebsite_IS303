#Levi Duke

#This file determines the routes of where the user will go
from .views import indexPageView
from django.urls import path
from .views import individualpersonPageView
from .views import missingpersonstablePageView
from .views import displayPersonPageView
#from . import views



urlpatterns = [  
    path("<int:id>/", displayPersonPageView, name="displayPerson"), 
    path("missingpersonstable/", missingpersonstablePageView, name="mptable"), 
    path("<str:Person>/", individualpersonPageView, name="individualperson"), 
    path("", indexPageView, name="index"),
] 

