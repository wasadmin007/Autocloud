from django import forms
import view 
from ..model.data import data

class NameForm(forms.Form):
    envname = forms.CharField(label='Env Name',max_length=20) 
    appname = forms.CharField(label='Application Name', max_length=20)
    OSFlavor = forms.CharField(label='OSFlavor', widget=forms.Select(choices=data().OSnames())) 
    OSversion = forms.FloatField(label='OSversion', widget=forms.Select(choices=data().LinuxOSverchoices()))
    TotalCPUS = forms.IntegerField(label='TotalCPUS', widget=forms.Select(choices=data().TotalCPUS()))
    OSBit = forms.IntegerField(label='OSbit', widget=forms.Select(choices=data().CPUTypes()))
    Servers = forms.CharField(label='Servers',  max_length=25, widget=forms.Select(choices=data().server_choices()))
    
    #envname = forms.CharField(label='Env Name',max_length=20) 
    ##appname = forms.CharField(label='Application Name', max_length=20)
    #OSFlavor = forms.FloatField(label='OSFlavor', widget=forms.Select(choices=data().OSnames())) 
    #OSversion = forms.FloatField(label='OSversion')
    #TotalCPUS = forms.IntegerField(label='TotalCPUS', )
    #OSBit = forms.IntegerField(label='OSbit' )
    #Servers = forms.CharField(label='Servers',)
    
    