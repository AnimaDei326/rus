import requests
from django.conf import settings
from django.shortcuts import render
import json


def blogs(request):
    offset = int(request.GET.get('offset', 0))
    batch_size = int(request.GET.get('batch_size', 9))
    response_blogs = requests.get('http://{}/blogs_/?batch=true&offset={}&batch_size={}'
                                  .format(settings.DOMAIN, offset, batch_size))
    blog_list = json.loads(response_blogs.text)['blogs']
    return render(request, 'rus_app/blogs.html', context=dict(blogs=blog_list))
