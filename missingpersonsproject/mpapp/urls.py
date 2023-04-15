#Levi Duke

#This file determines the routes of where the user will go
from .views import indexPageView
from django.urls import path
<<<<<<< HEAD
from .views import individualpersonPageView
from .views import missingpersonstablePageView

urlpatterns = [  
    path("<int:id>/", displayStudentPageView, 
name="displayStudent"), 
    path("showStudents/", showStudentsPageView, name="showStudents"), 
    path("<str:sName>/", displayPageView, name="displayScreen"), 
    path("", indexPageView, name="index"),
] 

urlpatterns = [
    path("",indexPageView, name="index"),
    path("mptable/", missingpersonstablePageView, name="mptable"  ),
    path("individualperson/", individualpersonPageView, name = "individualperson"),
=======


urlpatterns = [
    path("",indexPageView, name="index")
>>>>>>> origin/master
]
