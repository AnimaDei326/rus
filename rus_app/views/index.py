import requests
from django.conf import settings
from django.shortcuts import render
import json


def index(request):
    response_gallery = requests.get('http://{}/gallery'.format(settings.DOMAIN))
    response_blog = requests.get('http://{}/blog'.format(settings.DOMAIN))
    gallery_list = json.loads(response_gallery.text)['gallery']
    blog_list = json.loads(response_blog.text)['blog']
    return render(request, 'rus_app/index.html', context=dict(gallery=gallery_list, blog=blog_list))
