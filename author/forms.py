
from django import forms
from .models import Author

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Author
        #fields = '_all_'
        fields = ['name','email','bio','phone_no']
        #exclude = ['bio']