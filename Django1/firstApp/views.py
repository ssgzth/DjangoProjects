from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world!, from the firstApp home view!")

def about(request):
    return HttpResponse("This is the about page of firstApp.")
# Create your views here.
