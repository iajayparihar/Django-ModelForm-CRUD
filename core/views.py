from django.shortcuts import render,redirect
from .forms import userForms
from .models import userModel


def index(request):
    form = userForms()
    alldata = userModel.objects.all()

    if request.method == 'POST':
        form = userForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request,'index.html',{'form':form,'data':alldata})


def updatee(request,id):
    data = userModel.objects.get(id = id)
    userModel.objects.filter(id=id).delete()
    form = userForms(instance=data)
    if request.method == 'POST':
        form = userForms(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'update.html',{'form':form})



def delete(request,id):
    userModel.objects.filter(id=id).delete()
    return redirect('/')