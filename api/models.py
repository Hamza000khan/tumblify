from django.db import models
from django.conf import settings
from django.utils import timezone

# Blog, Bookmark, Video Embed, Image embed, Github Embed, Images(multiple images in the same blog post), Quote.


class Blogger(models.Model):
    blogger = models.CharField(max_length=200)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.blogger


class Blog(models.Model):
    Bookmark = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    image_embed = models.ImageField(upload_to='emb_images', default='')
    video_embed = models.FileField(upload_to='video/')
    gist_embed = models.CharField(max_length=200)
    Blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Bookmark


class Images(models.Model):
    blog = models.ForeignKey(Blog, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.blog.Bookmark


class Blogs(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=None, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    images = models.ForeignKey(Images, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
