from django.shortcuts import HttpResponse
from . import views

# Create your views here.

def add_author(request):
    return HttpResponse("This is the Add Author page")

