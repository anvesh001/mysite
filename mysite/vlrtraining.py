from django.http import HttpResponse
#from django.http import HttpResponse
from django.shortcuts import render
def ram(request):
    return render(request,"h1ram.html",{'vlr':'8867818491'})


def wel(request):
    return HttpResponse('<h1>vlr training<h1>')