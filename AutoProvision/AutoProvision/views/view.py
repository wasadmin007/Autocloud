from django.shortcuts import render
from django.template.defaulttags import register
from .forms.jbossorder import jbossForm
from django.http.response import HttpResponse
from ..model.data import data


#class AutoCompleteZones():#autocomplete.Select2QuerySetView):
#	def autocompletezones():
#		zones = data().get_avalable_zones('us-east-1')
#		return zones
def title():
    return 'AutoCloud'

def tempalte(request):
    fileTemp = 'index.html'
    return render(request,fileTemp, {'formset': 'Praveen Testting' , 'Tabs': data().data_static() ,'title':title()})

def awszones(request):
    region = request.GET.get('region')
    #region = 'us-east-1'
    fileTemp = 'awszones.tpl'
    dat = list(data().get_avalable_zones_ax(region))
    return render(request,fileTemp, { 'zones': dat})
    #return render(request,fileTemp, {'cities': zones})
def orderview(request):
    fileTemp = 'vieworder.tpl'
    return render(request,fileTemp, {'formset': 'Praveen Testting' , 'Tabs': data().data_static() ,'title':title()})


