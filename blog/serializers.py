from rest_framework.serializers import ModelSerializer
from django.utils import timezone

from blog.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'text', 'published_date']


