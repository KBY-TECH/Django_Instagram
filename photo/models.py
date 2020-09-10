from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_photos')

    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']
    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self): #객체 상세 페이지 주소 반환 , 상세 화면으로 이동하는 링크를 만들때 호출
        return reverse('photo:detail', args=[str(self.id)])