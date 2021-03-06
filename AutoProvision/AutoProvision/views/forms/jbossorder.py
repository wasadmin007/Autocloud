from django import forms

from ...model.data import data
#from dal import autocomplete
import logging
logger = logging.getLogger(__name__)
class jbossForm(forms.Form):
        envname = forms.CharField(label='Env Name',max_length=20) 
        appname = forms.CharField(label='Application Name', max_length=20)
        Cloud = forms.CharField(label='ClodProvider', widget=forms.Select(choices=data().cloud_choices()))
        AWSRegions = forms.CharField(label='AWSRegions', widget=forms.Select(choices=data().get_avalable_regions_choices()), initial='us-east-1')
        AWSZones = forms.CharField(label='AWSZones', widget=forms.Select(choices=data().get_avalable_zones('us-east-1')), initial='us-east-1a')
        OSFlavor = forms.CharField(label='OSFlavor', widget=forms.Select(choices=data().OSnames()))
        OSversion = forms.FloatField(label='OSversion', widget=forms.Select(choices=data().LinuxOSverchoices()))
        TotalCPUS = forms.IntegerField(label='TotalCPUS', widget=forms.Select(choices=data().TotalCPUS()))
        OSBit = forms.IntegerField(label='OSbit', widget=forms.Select(choices=data().CPUTypes()))
        Servers = forms.CharField(label='Servers',  max_length=25, widget=forms.Select(choices=data().server_choices()), initial='Jboss')
        #envname = forms.CharField(label='Env Name',max_length=20) 
        ##appname = forms.CharField(label='Application Name', max_length=20)
        #OSFlavor = forms.FloatField(label='OSFlavor', widget=forms.Select(choices=data().OSnames())) 
        #OSversion = forms.FloatField(label='OSversion')
        #TotalCPUS = forms.IntegerField(label='TotalCPUS', )
        #OSBit = forms.IntegerField(label='OSbit' )
        #Servers = forms.CharField(label='Servers',)
        class Meta:
           model = data().get_avalable_regions_choices()
           fields = ( 'AWSRegions', 'AWSZones')
