
from django.http import HttpResponse


def hola (request):
    return HttpResponse('<h1> Esto es nuevo</h1>')