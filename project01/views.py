from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello, world!')
