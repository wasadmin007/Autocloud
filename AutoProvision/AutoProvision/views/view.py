from django.shortcuts import render
from django.template.defaulttags import register
from .jbossorder import NameForm
from django.http.response import HttpResponse
from ..model.data import data

def title():
    return 'AutoCloud'
def index(request):
    a = add(3, 4)
    return HttpResponse("Hello, world. You're at the polls index." + str(a))
def add(b,c):
    a = b + c
    return a
#  
def tempalte(request):
    fileTemp = 'index.html'
    return render(request,fileTemp, {'formset': 'Praveen Testting' , 'Tabs': data().data_static() ,'title':title()})
#


def orderview(request):
    fileTemp = 'vieworder.tpl'
    return render(request,fileTemp, {'formset': 'Praveen Testting' , 'Tabs': data().data_static() ,'title':title()})
#

