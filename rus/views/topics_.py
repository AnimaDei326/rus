from django.http import JsonResponse
from ..models.topic import Topic


def topics_(request):
    try:
        topic_list = Topic.objects.filter(active=True).order_by('sort')
    except Topic.DoesNotExist:
        return []

    return JsonResponse(dict(
        topics=
        [
            dict(id=topic.id,
                 url=request.build_absolute_uri(topic.picture.url),
                 title=topic.title,
                 code=topic.code,
                 description=topic.description)
            for topic in topic_list]
    ))
