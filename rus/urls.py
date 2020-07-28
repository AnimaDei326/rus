"""rus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path
from django.contrib import admin
from rus.views.form import get_contact
from rus.views.blogs_ import blogs_
from rus.views.blog_ import blog_
from rus.views.blog import blog
from rus.views.blogs import blogs
from rus.views.gallery_ import gallery_
from rus.views.topic_ import topic_
from rus.views.topics_ import topics_
from rus.views.topic import topic
from rus.views.topics import topics
from rus.views.index import index
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('gallery_/', gallery_, name='gallery_'),
    path('blogs_/', blogs_, name='blogs_'),
    path('blogs/', blogs, name='blogs'),
    path('blog_/<str:code>/', blog_, name='blog_'),
    path('blog/<str:code>/', blog, name='blog'),
    path('topic_/<str:code>/', topic_, name='topic_'),
    path('topic/<str:code>/', topic, name='topic'),
    path('topics_/', topics_, name='topics_'),
    path('topics/', topics, name='topics'),
    path('get_contact/', get_contact, name='get_contact'),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
