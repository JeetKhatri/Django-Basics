from django.shortcuts import render
from travello.models import Destination
# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = 'Ahmedabad'
    dest1.desc = 'Ahmedabad description'
    dest1.price = 500

    dest2 = Destination()
    dest2.name = 'Mumbai'
    dest2.desc = 'Mumbai description'
    dest2.price = 700

    dest3 = Destination()
    dest3.name = 'Bangalore'
    dest3.desc = 'Bangalore description'
    dest3.price = 1000
    return render(request, 'index.html', {'dest1' : dest1, 'dest2' : dest2, 'dest3' : dest3})
