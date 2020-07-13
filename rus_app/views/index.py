import requests
from django.conf import settings
from django.shortcuts import render
import json


def index(request):
    response_gallery = requests.get('http://{}/gallery_'.format(settings.DOMAIN))
    response_blog = requests.get('http://{}/blogs_'.format(settings.DOMAIN))
    gallery_list = json.loads(response_gallery.text)['gallery']
    topic_list = json.loads(response_gallery.text)['topics']
    blog_list = json.loads(response_blog.text)['blogs']
    return render(request, 'rus_app/index.html', context=dict(
        gallery=gallery_list, topic=topic_list, blog=blog_list))
