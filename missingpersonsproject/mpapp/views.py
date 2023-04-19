from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import Person


# Create your views here.
def indexPageView(request):
    return render(request, 'mpapp/index.html')

def missingpersonstablePageView(request):
    db_person = Person.objects.all() 
    print("Data fetched from database: ", db_person)  # Add this line
    context = {
        "data" : db_person
    }
    return render(request, 'mpapp/missingpersonstable.html', context)

def individualpersonPageView(request, id):
   db_person = Person.objects.all() 
   context = {
            "data" : db_person
    }
   return render(request, 'mpapp/individualperson.html', context)


def displayPersonPageView(request, id) :
    missingperson = Person.objects.get(id=id)   
    context = {
            "data" : missingperson
    }
    return render(request, 'mpapp/displayPerson.html', context)
