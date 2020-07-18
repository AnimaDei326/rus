from django.http import JsonResponse
from ..models.blog import Blog


def blogs_(request):
    offset = int(request.GET.get('offset', 0))
    batch_size = int(request.GET.get('batch_size', 0))
    is_main_page = request.GET.get('is_main_page', False)
    blog_list = Blog.objects.filter(active=True).order_by('sort')

    if offset:
        blog_list = blog_list.filter(id__gt=offset)

    if is_main_page:
        blog_list = blog_list.filter(show_on_main_page=True)

    if batch_size:
        blog_list = blog_list[:batch_size]

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
