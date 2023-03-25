from rest_framework import serializers
from ...models import Post

# class PostSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ["id","image","title","content","created_date","published_date"]
        fields = "__all__"