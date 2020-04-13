from django.http import JsonResponse
from ..models.gallery import Gallery


def gallery(request):
    gallery_list = Gallery.objects.filter(active=True).order_by('sort')
    return JsonResponse(dict(
        gallery=[
            dict(
                id=pic.id,
                picture=request.build_absolute_uri(pic.picture.url),
                title=pic.title,
                description=pic.description,
                show_on_main_page=pic.show_on_main_page,
                show_in_slider=pic.show_in_slider,
            ) for pic in gallery_list
        ]
    ))
