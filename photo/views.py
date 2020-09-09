from django.shortcuts import render
from django.views.generic.edit import *
from .models import *
# Create your views here.


def list(request):
    photos=Photo.objects.all()
    return render(request,'photo/list.html',{'photos':photos})
