from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
<<<<<<< HEAD
    return render(request, 'mpapp/index.html')

def missingpersonstablePageView(request):
    return render(request, 'mpapp/missingpersonstable.html')

def individualpersonPageView(request):
    return render(request, 'mpapp/individualperson.html')
=======
    return render(request, 'mpapp/index.html')
>>>>>>> origin/master
