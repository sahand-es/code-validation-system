from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def load_page(request):
    return render(request, "html/main/codepage.html")
# Create your views here.
