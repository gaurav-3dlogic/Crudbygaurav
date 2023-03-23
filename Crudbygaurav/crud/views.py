from django.http import HttpResponse
from django.shortcuts import redirect, render
from crud.forms import UserForm
from django.http import HttpResponse
from crud.models import Gaurav

# Create your views here.


def insert(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid:
            try:
                form.save()
                return HttpResponse("<h1>Data Sent to DataBase...<h1>")
            except:
                pass 

    form = UserForm()
    return render(request,'index.html',{'form':form}) 


def show(request):
    users = Gaurav.objects.all()
    return render(request,'show.html',{'users':users})  

def delete(request,id):
    user = Gaurav.objects.get(id=id)
    user.delete()
    return redirect('/show')

def edit(request,id):
    user = Gaurav.objects.get(id=id)
    return render(request,'edit.html',{'user':user})
    
def update(request,id):
    user = Gaurav.objects.get(id=id)
    form = UserForm(request.POST,instance=user)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'user':user})


