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
    form_contact = requests.get('http://{}/get_contact'.format(settings.DOMAIN)).text
    q = 1
    return render(request, 'rus_app/index.html', context=dict(
        gallery=gallery_list, topic=topic_list, blog=blog_list, form_contact=form_contact))
