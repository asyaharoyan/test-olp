from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse("These are the courses")