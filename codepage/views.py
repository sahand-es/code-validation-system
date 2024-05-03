from django.http import HttpResponse
from django.shortcuts import render


def say_hello(request):
    return HttpResponse("hello")

# Create your views here.
