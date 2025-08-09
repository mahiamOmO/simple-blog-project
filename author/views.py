from django.shortcuts import render
from . import views
from . import forms


# Create your views here.

def add_author(request):
    author_form = forms.AuthorForm()
    return render(request,'add_author_html', {'form': author_form})

