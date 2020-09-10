from django.shortcuts import render
from .forms import *
# Create your views here.


def register(request):
    if request.method=="POST":
        form=RegisterFrom(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request,'registration/registerdone.html',{'new_user':user})
    else:
        form=RegisterFrom()
    return render(request,'registration/register.html',{'form':form})
