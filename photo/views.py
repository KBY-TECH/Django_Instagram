from django.shortcuts import render, redirect
from django.views.generic.edit import *
from .models import *
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def list(request):
    photos=Photo.objects.all()
    return render(request,'photo/list.html',{'photos':photos})


class PhotoUploadView(LoginRequiredMixin,CreateView):
    model=Photo
    fields=['photo','text']
    template_name='photo/upload.html'

    #입려된 데이터가 올바른가?
    def form_valid(self,form):
        form.instance.author_id=self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')

        else:
            return self.render_to_response({'form':form})

class PhotoDeleteView(LoginRequiredMixin,DeleteView):
    model = Photo
    success_url = '/'
    template_name='photo/delete.html'


class PhotoUpdateView(UpdateView):
    model = Photo
    fields =['photo','text']
    template_name = 'photo/update.html'

