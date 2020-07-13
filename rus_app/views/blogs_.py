from django.http import JsonResponse
from ..models.blog import Blog


def blogs_(request):
    blog_list = Blog.objects.filter(active=True, show_on_main_page=True).order_by('sort')
    return JsonResponse(dict(
        blogs=[
            dict(
                id=item.id,
                picture=request.build_absolute_uri(item.picture.url),
                title=item.title,
                code=item.code,
                preview_text=item.preview_text,
                show_on_main_page=item.show_on_main_page,
                text=item.text,
                last_updated=item.last_updated.strftime("%d.%m.%Y"),
            ) for item in blog_list
        ]
    ))
