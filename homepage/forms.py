from django import forms
from .models import Person

class PersonModelForm(forms.ModelForm):   
    class Meta:
        model = Person
        fields = [
            'name',
            'email',
            'job_title',
            'bio',
        ]
