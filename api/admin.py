from django.contrib import admin
from .models import Blog, Blogger, Images, Blogs

admin.site.register(Blogger)
# admin.site.register(Images)


class PostImageAdmin(admin.StackedInline):
    model = Images


@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    # for enabling  one-to-many relationship for the images
    inlines = [PostImageAdmin]

    class Meta:
        model = Blog
