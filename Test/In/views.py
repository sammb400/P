from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request) :
    
    #context = {'dat': dat }
    return render (request, 'In/Inn.html')
