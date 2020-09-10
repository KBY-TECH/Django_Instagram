from django.contrib import admin
from .models import *
# Register your models here.

class photoAdmin(admin.ModelAdmin):
    list_display = ['id','author','created','updated']
    raw_id_fields = ['author'] # 작성자 고르기가 아닌 찾기 (만약 회원이 만명이상이면.. 힘듬)
    list_filter = ['created','updated','author']
    search_fields = ['text','created','author__username'] #author는 자체가 객체.
    ordering = ['-updated','-created'] # db 모델과는 다르다 admin 은 따로 db는 따로

admin.site.register(Photo,photoAdmin)
