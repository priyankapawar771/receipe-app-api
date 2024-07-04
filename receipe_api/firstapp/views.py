from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def display(request):
        s= '<h1>Hello user welcome to django project</h1>'
        dateTime = datetime.datetime.now()
        response = str(dateTime) + " " + s
        return HttpResponse(response)

