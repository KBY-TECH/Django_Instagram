from django.contrib import admin
from .models import *
# Register your models here.

class photoAdmin(admin.ModelAdmin):
    list_display = ['id','author','created','updated']
    raw_id_fields = ['author']
    list_filter = ['created','updated','author']
    search_fields = ['text','created','author__username']
    ordering = ['-updated','-created'] # db 모델과는 다르다 admin 은 따로 db는 따로

admin.site.register(Photo,photoAdmin)
