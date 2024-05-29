from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'created_at', 'modified_at')
        read_only_fields = ('author', 'created_at', 'modified_at',)