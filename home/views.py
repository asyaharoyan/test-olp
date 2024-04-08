# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


# def home(request):
#     return HttpResponse("Hello, Blog!")

from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'home/index.html'