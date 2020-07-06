import requests
from django.conf import settings
from django.shortcuts import render
import json


def topics(request):
    response_topic = requests.get('http://{}/topics_/'.format(settings.DOMAIN))
    topic_list = json.loads(response_topic.text)['topics']
    return render(request, 'rus_app/topics.html', context=dict(topics=topic_list))
