from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializers
from blog.models import Post
from django.shortcuts import get_object_or_404


@api_view()
def api_post_list_view(request):
    return Response({"ok": "ali"})


@api_view()
def api_post_detail_view(request, id):
    
    post = get_object_or_404(Post,pk=id)
    serializer = PostSerializers(post)
    return Response(serializer.data)
