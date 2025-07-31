from django.shortcuts import render
from django.http import HttpResponse

def second_home(request):
    return HttpResponse("Hello, world!, from the secondApp home view!")

def second_about(request):
    return HttpResponse("This is the about page of secondApp.")
