from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def add_index(request):
    a = request.GET['a']
    b = request.GET['b']
    s = int(a) + int(b)
    return HttpResponse('a + b is equal to ' + str(s))
