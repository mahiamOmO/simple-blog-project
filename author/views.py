from django.shortcuts import render, redirect
from .forms import ProfileForm

def add_author(request):
    if request.method == 'POST':
        author_form = ProfileForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('add_author')
    else:
        author_form = ProfileForm()
    return render(request, 'add_author_html', {'form': author_form})
