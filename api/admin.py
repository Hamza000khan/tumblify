from django.contrib import admin
from .models import Blog,  Images

# admin.site.register(Blogger)
# admin.site.register(Blogs)


class PostImageAdmin(admin.StackedInline):
    model = Images


@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    # for enabling  one-to-many relationship for the images
    inlines = [PostImageAdmin]

    class Meta:
        model = Blog
