from django.http import JsonResponse
from ..models.gallery import Gallery


def gallery(request):
    gallery_list = Gallery.objects.filter(active=True).order_by('sort')
    return JsonResponse(dict(
        gallery=[
            dict(
                id=item.id,
                picture=request.build_absolute_uri(item.picture.url),
                title=item.title,
                description=item.description,
                show_on_main_page=item.show_on_main_page,
                show_in_slider=item.show_in_slider,
            ) for item in gallery_list
        ]
    ))
