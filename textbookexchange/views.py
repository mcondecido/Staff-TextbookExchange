from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi all class!!! Hello, world. You are my everything!  :heart:")
