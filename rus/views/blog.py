import requests
from django.conf import settings
from django.shortcuts import render
import json


def blog(request, code):
    response_topic = requests.get('http://{}/blog_/{}/'.format(settings.DOMAIN, code))
    blog_data = json.loads(response_topic.text)['blog']
    return render(request, 'rus/blog.html', context=dict(blog=blog_data))
