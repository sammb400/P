from urllib import response
from django.shortcuts import render

# Create your views here.
def first(response):
    return render (response, 'base.html')
