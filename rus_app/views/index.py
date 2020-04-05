import requests
from django.conf import settings
from django.shortcuts import render
import json


def index(request):
    response = requests.get('http://{}/gallery'.format(settings.DOMAIN))
    gallery_list = json.loads(response.text)['gallery']
    return render(request, 'rus_app/index.html', context=dict(gallery=gallery_list))
