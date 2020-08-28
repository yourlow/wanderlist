from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index(request):
   # template = loader.get_template('templates/base.html')
   #return render(request, "base.html")
    return HttpResponse("Hello world, you're at the wanderlist index, just a test")

def matt(request):
    return HttpResponse("pleeease work")

def brian(request, id):
    all_users = Activity.objects
    return HttpResponse(all_users)

def add_business(request, business_name, business_password):
    business_instance = Business.objects.create(name=business_name, password=business_password)
    return HttpResponse("added" + business_name)

def get_business_by_id(request, business_id):
    get_activity = Business.objects.all().filter(id=business_id)
    return HttpResponse(get_activity)
