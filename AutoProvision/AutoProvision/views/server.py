from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.defaulttags import register
from .jbossorder import NameForm
from django.http.response import HttpResponse
from django.views.decorators.http import require_POST
from ..model.data import data

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            if not request.POST.get("envname"):
                 return HttpResponse('Environment Name Should be String    '+ request.POST.get("envname"))
                
            if not request.POST.get("appname"):
                  return HttpResponse('Application Name Should be String    '+ request.POST.get("appname"))
          
            
            Values_post = ''+request.POST.get("envname")+' '+request.POST.get("appname")
            return HttpResponse('Thank you For Choosing Auto Cloud Following Values Are Passed to Provision Jboss '+Values_post)
        else:
            return HttpResponse('Form is Invalid    ' , form  )

    # if a GET (or any other method) we'll create a blank form
    else:
        forms = NameForm()  
        return render(request, 'jboss.html', {'forms': forms})


    