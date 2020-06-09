from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def info(request):
    return render(request, 'info.html')

def register(request):
    return render(request, 'register.html')

def register(request):
    return render(request, 'register_done.html')
