from django.contrib import admin
from .models import Blog, Blogger, Images

# admin.site.register(Blog)
admin.site.register(Blogger)

#


class PostImageAdmin(admin.StackedInline):
    model = Images


@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    # for enabling  one-to-many relationship for the images
    inlines = [PostImageAdmin]

    class Meta:
        model = Blog


@admin.register(Images)
class PostImageAdmin(admin.ModelAdmin):
    pass
