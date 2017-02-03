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
from views import view
from views import server

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view.tempalte, name='index'),
    url(r'^Jboss', server.jboss, name='jboss'), 
    url(r'^Tomcat', server.tomcat, name='Tomcat'),
    url(r'^Apache', server.apache, name='Apache'),
    url(r'^WAS', server.WAS, name='WAS'),
    url(r'^IHS', server.IHS, name='IHS'),
    url(r'^WebLogic', server.weblogic, name='Weblogic'),
    url(r'^vieworder', view.orderview, name='orderview'),
  
]
