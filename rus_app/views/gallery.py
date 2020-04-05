from django.http import JsonResponse
from ..models.gallery import Gallery


def gallery(request):
    gallery_list = Gallery.objects.filter(active=True)
    return JsonResponse(dict(
        gallery=[
            dict(
                id=pic.id,
                picture=request.build_absolute_uri(pic.picture.url),
                description=pic.description,
            ) for pic in gallery_list
        ]
    ))
