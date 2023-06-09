from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView


def index(request):
    return render(request, 'index.html')

def goldline(request):
    return render(request, 'goldline.html')

def m249(request):
    return render(request, 'm249.html')

def automag(request):
    return render(request, 'automag.html')

def beretta(request):
    return render(request, 'beretta.html')