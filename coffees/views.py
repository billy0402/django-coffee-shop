from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('<h1>咖啡</h1>')
