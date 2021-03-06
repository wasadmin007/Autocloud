"""AutoProvision URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import view
from .views import server
from django.urls import path

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('', view.tempalte, name='index'),
    path('Jboss', server.jboss, name='jboss'), 
    path(r'Tomcat', server.tomcat, name='Tomcat'),
    path(r'Apache', server.apache, name='Apache'),
    path(r'WAS', server.WAS, name='WAS'),
    path(r'IHS', server.IHS, name='IHS'),
    path(r'WebLogic', server.weblogic, name='Weblogic'),
    path(r'vieworder', view.orderview, name='orderview'),
    path('zones/', view.awszones, name='awszones'),
    #path('zones/<region>', view.awszones, name='awszones')
]
