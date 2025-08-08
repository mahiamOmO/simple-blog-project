from django.contrib import admin
from django.urls import path,include
from . import views

urlspattern = [

    path('add/',views.add_profile,name='add_profile')

]