from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hi, glad to be back my King!')
