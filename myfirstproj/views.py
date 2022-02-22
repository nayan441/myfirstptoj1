from django.http import HttpResponse, HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')