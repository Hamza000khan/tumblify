from django.db import models
from django.conf import settings
from django.utils import timezone


class Blog(models.Model):
    bookmark = models.CharField(max_length=200, blank=True, default='')
    quote = models.TextField(blank=True, default='')
    image_embed = models.ImageField(
        upload_to='emb_images', blank=True, default='')
    video_embed = models.FileField(upload_to='video/')
    gist_embed = models.CharField(max_length=200, blank=True, default='')
    user = models.ForeignKey(
        'auth.User', related_name='blog', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.bookmark
