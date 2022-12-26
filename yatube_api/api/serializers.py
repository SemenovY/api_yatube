"""Сериализаторы для моделей пост."""
from rest_framework import serializers
from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post."""
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'text', 'group', 'author', 'image', 'pub_date')


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'post', 'created')

