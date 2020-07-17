from django.contrib import admin
from .models import Gallery
from .models import Blog
from .models import Topic
from .models import FormContact


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(FormContact)
class FormContactAdmin(admin.ModelAdmin):
    readonly_fields = ['date_create', ]
    list_display = ['subject', 'done', 'date_create', ]
