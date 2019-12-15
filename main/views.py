from django.shortcuts import render,redirect

from .forms import DataForm
from .models import Data

# Create your views here.
def add_detail(request):
    form = DataForm()
    if request.method == "POST":
        form = DataForm(request.POST or None)
        if form.is_valid():
            d = form.cleaned_data
            if Data.objects.filter(usr_name = d['usr_name'],email = d['email'],number = d['number']).exists():
                return render(request,"create.html",{"form":form,"status":"The given data already exist"})
            form.save()
            form = DataForm()
            return redirect(saved_successfully)
    return render(request,"create.html",{"form":form})

def saved_successfully(request):
    return render(request,"output.html",{"detail":"Saved"})

def retrive(request):
    obj = Data.objects.all()
    return render(request,"show.html",{"obj":obj})

def delete(request):
    form = DataForm(request.POST or None)
    if form.is_valid() :
        d = form.cleaned_data
        if Data.objects.filter(usr_name = d['usr_name'],email = d['email'],number = d['number']).exists():
            delete_from_db(d)
            form = DataForm()
            return redirect(deleted_successfully)
        else:
            return render(request,"delete.html",{"form":form,"status":"No matching data fouond! Enter data."})
    return render(request,"delete.html",{"form":form})


def deleted_successfully(request):
    return render(request,"output.html",{"detail":"Deleted"})

def delete_from_db(d):
    obj = Data.objects.get(usr_name = d['usr_name'],email = d['email'],number = d['number'])
    obj.delete()

def update(request):
    form = DataForm(request.POST or None)
    if form.is_valid():
        d = form.cleaned_data
        if Data.objects.filter(usr_name = d['usr_name'],email = d['email'],number = d['number']).exists():
            delete_from_db(d)
            return redirect("/create")
        else:
            return render(request,"update.html",{"form":form,"notfound":"The given data does not exist in the table"})
    return render(request,"update.html",{"form":form,"found":"","notfound":""})
