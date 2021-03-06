"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

# delete view
from django.views.generic.detail import DetailView
from .models import Photo
# 2차 url file
app_name = 'photo'

urlpatterns = [
    path('',list,name='list'),
    path('upload/',PhotoUploadView.as_view(),name='upload'),
    path('detail/<int:pk>/',DetailView.as_view(
        model=Photo,template_name='photo/detail.html'
    )
         ,name='detail'),
    path('delete/<int:pk>/',PhotoDeleteView.as_view(),name='delete'),
    path('update/<int:pk>/',PhotoUpdateView.as_view(),name='update'),
]
