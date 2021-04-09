from django.shortcuts import render
from django.views.generic import CreateView
from .models import Person
from .forms import PersonModelForm

# Create your views here.

def homepage(request):
    form = PersonModelForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'index.html', context)