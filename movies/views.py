from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# main page
def index(request):
    return HttpResponse('Hello World')
