from django.shortcuts import render
from django.HttpResponse import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hi')
