from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Animal


def index_view(request):
    return render(request, 'application/index.html')


class AnimalList(ListView):
    model = Animal


class AnimalDetail(DetailView):
    model = Animal
