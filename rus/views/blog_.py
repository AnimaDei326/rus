from django.http import JsonResponse
from ..models.blog import Blog


def blog_(request, code):
    try:
        blog_data = Blog.objects.get(active=True, code=code)
    except Blog.DoesNotExist:
        return []

    return JsonResponse(dict(
        blog=dict(
            id=blog_data.id,
            picture=request.build_absolute_uri(blog_data.picture.url),
            title=blog_data.title,
            text=blog_data.text,
            last_updated=blog_data.last_updated.strftime("%d.%m.%Y"),
        )
    ))
