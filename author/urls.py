from django.contrib import admin
from django.urls import path,include

urlspattern = [

    path('add/',views.add_author,name='add_author')

]