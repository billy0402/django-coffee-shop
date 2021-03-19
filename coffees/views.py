from django.shortcuts import render

from .models import Coffee


# Create your views here.
def index(request):
    coffees = Coffee.objects.all()
    return render(request, 'coffees/index.html', {'coffees': coffees})
