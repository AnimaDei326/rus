import requests
from django.conf import settings
from django.shortcuts import render
import json


def topic(request, code):
    response_topic = requests.get('http://{}/topic_/{}/'.format(settings.DOMAIN, code))
    topic_data = json.loads(response_topic.text)['topic']
    gallery = json.loads(response_topic.text)['gallery']

    return render(request, 'rus/topic.html', context=dict(topic=topic_data, gallery=gallery))
