from django.shortcuts import render
from .models import JobVacations
from .forms import JobForm,JobForm2
from django.shortcuts import (get_object_or_404,HttpResponseRedirect)
import requests

def URLshorten(request):

    val = request.POST.get('url_val')


    url = "https://url-shortener-service.p.rapidapi.com/shorten"

    payload = {"url": val}
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "6048b1f9f0msh6393f3aeec90d8dp1dce27jsn6c0a696ccd4a",
        "X-RapidAPI-Host": "url-shortener-service.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    res = response.json()

    return render(request, 'service.html', {'result': res})




def HomePage(request):
    return render(request, "home.html")

def VacationPage(request):
    val= JobVacations.objects.all()
    return render(request, "vacation.html" ,{'val':val})

def DetailPage(request, pk):
    el = JobVacations.objects.get(pk=pk)
    return render(request, "detail.html" , {'el':el})
def EditPage(request,pk):
    detail={}
    obj= get_object_or_404(JobVacations, pk=pk)
    form = JobForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    detail["form"]=form
    return render(request, "edit.html", detail)

def DeletePage(request,pk):
    obj= get_object_or_404(JobVacations, pk=pk)
    if request.method=='POST':
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "delete.html")
def CreatePage(request):
    context = {}
    form =JobForm2(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context['form'] = form
    return render(request, "create.html", context)



