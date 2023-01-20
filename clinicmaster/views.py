from django.http import HttpResponse  
from django.shortcuts import render  
from setup.models import Allergies
from django.template import loader


mytitle ="Clinic Master" 

def allergies_Page(request):
     allergies = Allergies.objects.all()
     print(allergies)
     template = loader.get_template('index.html')
     context = {'myallergies': allergies,"title" : "Allergies"}
     mytitle ={"title" : "Allergies",}
     return render(request,'index.html',context)

def patients_Page(request):
    return render(request, "patients.html",{"title" : "Clinic Master"})

def patientsGeneralPage(request):
    return render(request, "patientsGeneral.html",{"title" : "Clinic Master"})

def visits_Page(request):
    return render(request, "visits.html",{"title" : "Clinic Master"})