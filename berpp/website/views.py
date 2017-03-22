from django.http import HttpResponse
from django.shortcuts import render

from .ec_forms import ECForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        
        return render(request, 'signup.html')

    return render(request, 'signup.html')
