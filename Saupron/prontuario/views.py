from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ficha_view(request):
    return render(request, 'ficha.html')

