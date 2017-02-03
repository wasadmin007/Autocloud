from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.defaulttags import register
from forms.jbossorder import jbossForm
from forms.tomcatorder import tomcatForm
from forms.apacheorder import apacheForm
from forms.wasorder import wasForm
from django.http.response import HttpResponse
from django.views.decorators.http import require_POST
from forms.weblogicorder import weblogicForm
from forms.ihsorder import ihsForm


def jboss(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = jbossForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            if not request.POST.get("envname"):
                 return HttpResponse('Environment Name Should be String    '+ request.POST.get("envname"))
                
            if not request.POST.get("appname"):
                  return HttpResponse('Application Name Should be String    '+ request.POST.get("appname"))
          
            
            Values_post = 'Environment '+request.POST.get("envname")+' Apllication '+request.POST.get("appname")
            return HttpResponse('Thank you For Choosing Auto Cloud Following Values Are Passed to Provision Jboss '+Values_post)
        else:   
            return HttpResponse('Form is Invalid    ' )

    # if a GET (or any other method) we'll create a blank form
    else:
        forms = jbossForm()
        return render(request, 'jboss.html', {'forms': forms})

def tomcat(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = tomcatForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            if not request.POST.get("envname"):
                 return HttpResponse('Environment Name Should be String    '+ request.POST.get("envname"))
                
            if not request.POST.get("appname"):
                  return HttpResponse('Application Name Should be String    '+ request.POST.get("appname"))
          
            
            Values_post = 'Environment '+request.POST.get("envname")+' Apllication '+request.POST.get("appname")
            return HttpResponse('Thank you For Choosing Auto Cloud Following Values Are Passed to Provision Tomcat '+Values_post)
        else:   
            return HttpResponse('Form is Invalid    ' )

    # if a GET (or any other method) we'll create a blank form
    else:
        forms = tomcatForm()
        return render(request, 'tomcat.html', {'forms': forms})
def apache(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = apacheForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            if not request.POST.get("envname"):
                 return HttpResponse('Environment Name Should be String    '+ request.POST.get("envname"))
                
            if not request.POST.get("appname"):
                  return HttpResponse('Application Name Should be String    '+ request.POST.get("appname"))
          
            
            Values_post = 'Environment '+request.POST.get("envname")+' Apllication '+request.POST.get("appname")
            return HttpResponse('Thank you For Choosing Auto Cloud Following Values Are Passed to Provision Apache '+Values_post)
        else:   
            return HttpResponse('Form is Invalid    ' )

    # if a GET (or any other method) we'll create a blank form
    else:
        forms = apacheForm()
        return render(request, 'apache.html', {'forms': forms})
    
def WAS(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = wasForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            if not request.POST.get("envname"):
                 return HttpResponse('Environment Name Should be String    '+ request.POST.get("envname"))
                
            if not request.POST.get("appname"):
                  return HttpResponse('Application Name Should be String    '+ request.POST.get("appname"))
          
            
            Values_post = 'Environment '+request.POST.get("envname")+' Apllication '+request.POST.get("appname")
            return HttpResponse('Thank you For Choosing Auto Cloud Following Values Are Passed to Provision WAS '+Values_post)
        else:   
            return HttpResponse('Form is Invalid    ' )

    # if a GET (or any other method) we'll create a blank form
    else:
        forms = wasForm()
        return render(request, 'tomcat.html', {'forms': forms})
def IHS(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ihsForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            if not request.POST.get("envname"):
                 return HttpResponse('Environment Name Should be String    '+ request.POST.get("envname"))
                
            if not request.POST.get("appname"):
                  return HttpResponse('Application Name Should be String    '+ request.POST.get("appname"))
          
            
            Values_post = 'Environment '+request.POST.get("envname")+' Apllication '+request.POST.get("appname")
            return HttpResponse('Thank you For Choosing Auto Cloud Following Values Are Passed to Provision IBM IHS '+Values_post)
        else:   
            return HttpResponse('Form is Invalid    ' )

    # if a GET (or any other method) we'll create a blank form
    else:
        forms = ihsForm()
        return render(request, 'tomcat.html', {'forms': forms})
    
    
def weblogic(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = weblogicForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            if not request.POST.get("envname"):
                 return HttpResponse('Environment Name Should be String    '+ request.POST.get("envname"))
                
            if not request.POST.get("appname"):
                  return HttpResponse('Application Name Should be String    '+ request.POST.get("appname"))
          
            
            Values_post = 'Environment '+request.POST.get("envname")+' Apllication '+request.POST.get("appname")
            return HttpResponse('Thank you For Choosing Auto Cloud Following Values Are Passed to Provision BEA WebLogic '+Values_post)
        else:   
            return HttpResponse('Form is Invalid    ' )

    # if a GET (or any other method) we'll create a blank form
    else:
        forms = weblogicForm()
        return render(request, 'apache.html', {'forms': forms})
    
    