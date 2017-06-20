# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.db.models import Q
# Create your views here.


def index(request):
	a = Info.objects.order_by('firstName')
	return render(request, 'records/home.html', {'record' : a})


def detail(request,d):
    n=Info.objects.get(id=d)
    return render(request,'records/detail.html',{'t':n})


def contact(request):
    
    if request.method == "POST":
        form = contactform(request.POST)
        # print form
        if form.is_valid():
            
            obj=Info(firstName=form.cleaned_data['firstName']
                            ,lastName=form.cleaned_data['lastName'],
                        )

            obj.save()

            
            return HttpResponseRedirect('/')
            
    else:
        form=contactform()
    return render(request,'records/contact.html',{'form':form})


def delete(request,d, name):
    n = Info.objects.get(id = d)
    n.delete
    return HttpResponse('deleted')


def edit(request,d,name):
    n = Info.objects.get(id=d)

    if request.method=="POST":
        form = contactform(request.POST, instance = n)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=contactform(instance = n)
    return render(request, 'records/edit.html', {'formobj': form})


def search(request):
    if request.method== 'POST':
        squery = request.POST['search_box']
        if squery:
            s = Info.objects.filter(Q(firstName__icontains = squery)| Q(lastName__icontains = squery))
            if s:
                return render(request, 'records/search.html',{'q':s})
            else:
                return render(request, 'records/notfound.html')
        else:
            return HttpResponseRedirect('/')