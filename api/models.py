from django.db import models
from django.conf import settings
from django.utils import timezone

# Blog, Bookmark, Video Embed, Image embed, Github Embed, Images(multiple images in the same blog post), Quote.


# class Blog(models.Model):
#     name = models.CharField(max_length=200)
#     title = models.CharField(max_length=200)
#     added_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     created_date = models.DateTimeField(default=timezone.now)
#     description = models.CharField(max_length=300)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     added_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     created_date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.title
