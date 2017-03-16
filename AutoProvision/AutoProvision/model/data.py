
import os
import django
from django.forms.models import model_to_dict
from ..AWSBOTO.awsec2 import awsec2
from ..AWSBOTO import connection as conn
import boto.ec2
awsec = awsec2()
class data():  
    def data_static(self):
        Tabs = { 'Provisions': { 'AppServers' : ['Jboss', 'Tomcat', 'WAS', 'WebLogic', 'IHS', 'Apache'],
                                 'Cloud_provders': ['AWS']  },
                'Logs':{},
                'Help':{},
                'Settings':{'users': 'praveen' }
            }
        return Tabs         
    def server_choices(self):
        listServer = self.data_static()
        cho = []
        for key, options in listServer.items():
           for key1, option in options.items():
             if key1 == 'AppServers':
               for choice in option:
                  cho.append((choice,choice),)
        return cho
    def cloud_choices(self):
        listServer = self.data_static()
        cho = []
        for key, options in listServer.items():
           for key1, option in options.items():
             if key1 == 'Cloud_provders':
               for choice in option:
                  cho.append((choice,choice),)
        return cho
    def get_all_regions(self):
        regions = boto.ec2.get_regions('ec2', region_cls=None, connection_cls=None)
        return regions
    def get_avalable_zones(self):
        cho = []
        for key  in awsec.get_all_zones():
            cho.append((key.name,key.name),)
        return cho
    def get_avalable_regions_choices(self):
        cho = []
        regions = self.get_all_regions()
        for key  in regions:
            cho.append((key.name,key.name),)
        return cho
           
    def LinuxOSverchoices(self):
       cho = []
       list = ['5','6','6.5','6.6','6.7','6.8','7']
       for i in list:
           cho.append((i,i),)
       return cho
    def TotalCPUS(self):
       cho = []
       for i in range(1,40):
           cho.append((i,i),)
       return cho    
    def CPUTypes(self):
       cho = []
       osList = ['64','32']
       for i in osList:
           cho.append((i,i),)
       return cho   
    
    def OSnames(self):
       cho = []
       osList = ['RHEL', 'CentOS', 'Windows', 'Ubuntu']
       for i in osList:
           cho.append((i,i),)
       return cho    
            
        
        
        
    #
    