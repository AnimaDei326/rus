from django.http import JsonResponse
from ..models.gallery import Gallery
from ..models.topic import Topic


def gallery_(request):
    topic_list = Topic.objects.filter(active=True, show_on_main_page=True).order_by('sort')
    gallery_list = Gallery.objects.filter(active=True).order_by('sort')

    for topic in topic_list:
        current_gallery = [item.id for item in gallery_list if item.topic == topic]
        topic.gallery_list = current_gallery

    return JsonResponse(dict(
        gallery=[
            dict(
                id=item.id,
                picture=dict(
                    id=item.id,
                    url=request.build_absolute_uri(item.picture.url),
                    title=item.title,
                    description=item.description,
                    show_in_slider=item.show_in_slider,
                )) for item in gallery_list
        ],
        topic=[
            dict(
                id=item.id,
                url=request.build_absolute_uri(item.picture.url),
                title=item.title,
                code=item.code,
                gallery_list=item.gallery_list
            ) for item in topic_list
        ]
    ))
