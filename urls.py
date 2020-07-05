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
from rus_app.views.blog_ import blog_
from rus_app.views.gallery_ import gallery_
from rus_app.views.topic_ import topic_
from rus_app.views.topic import topic
from rus_app.views.index import index
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('gallery_/', gallery_, name='gallery_'),
    path('blog_/', blog_, name='blog_'),
    path('topic_/<str:code>/', topic_, name='topic_'),
    path('topic/<str:code>/', topic, name='topic'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
