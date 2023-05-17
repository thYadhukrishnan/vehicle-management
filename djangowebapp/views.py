from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse("About page")

def course(request,id):
    return HttpResponse(id)

def home(request):
    data={
        'title':'Home Page',
        'list':['java','php','python']
    }
    return render(request,"home.html",data)