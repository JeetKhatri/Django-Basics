from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {'name':'Jeet'})

def add(request):
    no1 = int(request.POST["no1"])
    no2 = int(request.POST["no2"])
    res = no1+no2
    return render(request, 'result.html', {'result':res})