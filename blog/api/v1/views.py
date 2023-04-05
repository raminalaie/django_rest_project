from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializers
from blog.models import Post
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView


# @api_view(["GET","POST"])
# @permission_classes([IsAuthenticated])
# def api_post_list_view(request):
#     if request.method == "GET":
#         post = Post.objects.filter(status=True)
#         serializer = PostSerializers(post, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


class PostList(APIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers
    
    def get(self,request):
        post = Post.objects.filter(status=True)
        serializer = PostSerializers(post, many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer = PostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
        

@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def api_post_detail_view(request, id):
    post = get_object_or_404(Post, pk=id,status = True)
    if request.method == "GET":
        serializer = PostSerializers(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializers(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
    