from django.http import JsonResponse
from ..models.gallery import Gallery
from ..models.topic import Topic


def topic_(request, code):
    try:
        topic_data = Topic.objects.get(code=code, active=True)
    except Topic.DoesNotExist:
        return []
    # TODO если будет 2 объекта

    gallery_list = Gallery.objects.filter(active=True, topic=topic_data).order_by('sort')

    return JsonResponse(dict(
        gallery=[
            dict(
                id=item.id,
                url=request.build_absolute_uri(item.picture.url),
                title=item.title,
                description=item.description,
                show_in_slider=item.show_in_slider,
            ) for item in gallery_list
        ],
        topic=
        dict(
            id=topic_data.id,
            url=request.build_absolute_uri(topic_data.picture.url),
            title=topic_data.title,
            description=topic_data.description,
        )
    ))
