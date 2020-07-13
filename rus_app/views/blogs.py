import requests
from django.conf import settings
from django.shortcuts import render
import json


def blogs(request):
    response_blogs = requests.get('http://{}/blogs_/'.format(settings.DOMAIN))
    blog_list = json.loads(response_blogs.text)['blogs']
    return render(request, 'rus_app/blogs.html', context=dict(blogs=blog_list))
