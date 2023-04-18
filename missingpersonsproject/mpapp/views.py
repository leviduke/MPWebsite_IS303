from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    return render(request, 'mpapp/index.html')

def missingpersonstablePageView(request):
    return render(request, 'mpapp/missingpersonstable.html')

def individualpersonPageView(request, id):
   db_person = oPerson.objects.all() 
   context = {
            "data" : db_person
    }
   return render(request, 'mpapp/individualperson.html', context)


def displayPersonPageView(request, id) :
    person = oPersons.objects.get(id=id)   
    context = {
            "data" : person
    }
    return render(request, 'mpapp/displayPerson.html', context)
