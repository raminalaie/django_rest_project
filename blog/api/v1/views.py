from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializers
from blog.models import Post
from django.shortcuts import get_object_or_404


@api_view(["GET","POST"])
def api_post_list_view(request):
    if request.method == "GET":
        post = Post.objects.filter(status=True)
        serializer = PostSerializers(post, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view()
def api_post_detail_view(request, id):
    
    post = get_object_or_404(Post, pk=id)
    serializer = PostSerializers(post)
    return Response(serializer.data)
