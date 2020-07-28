import requests
from django.conf import settings
from django.shortcuts import render
import json
from django.http import HttpResponse

def index(request):
    
    response_gallery = requests.get('http://{}/gallery_'.format(settings.DOMAIN))
    response_blog = requests.get('http://{}/blogs_/?batch_size=3&is_main_page=true'.format(settings.DOMAIN))
    gallery_list = []
    #return HttpResponse('ok1')
    topic_list = []
    if response_gallery.status_code == 200:
        gallery_list = json.loads(response_gallery.text)['gallery']
        topic_list = json.loads(response_gallery.text)['topics']
   
    blog_list = [] 
    if response_blog.status_code == 200:
        blog_list = json.loads(response_blog.text)['blogs']
    form_contact = requests.get('http://{}/get_contact'.format(settings.DOMAIN)).text
    return render(request, 'rus/index.html', context=dict(
        gallery=gallery_list, topic=topic_list, blog=blog_list, form_contact=form_contact))
