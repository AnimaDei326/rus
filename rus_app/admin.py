from django.contrib import admin
from .models import Gallery
from .models import Blog
from .models import Topic


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass
