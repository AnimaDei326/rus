from django.contrib import admin
from .models import Gallery
from .models import Blog
from .models import Topic
from .models import FormContact


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'sort', 'show_in_slider', ]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'sort', 'show_on_main_page', ]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'sort', 'show_on_main_page', ]


@admin.register(FormContact)
class FormContactAdmin(admin.ModelAdmin):
    readonly_fields = ['date_create', ]
    list_display = ['email', 'subject', 'done', 'date_create', ]

