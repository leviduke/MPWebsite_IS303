from django.apps import AppConfig
from django.urls import path
from .views import indexPageView, missingpersonstable.html,
individualpersonpageview

urlpatterns = [  
    path("showPerson/", showStudentsPageView, 
name="showStudents"), 
    path("<str:sName>/", displayPageView, name="displayScreen"), 
    path("", indexPageView, name="index"),
] 

class MpappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mpapp'
