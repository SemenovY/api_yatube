"""Сериализаторы для моделей пост."""
from rest_framework import serializers
from posts.models import Comment, Group, Post


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели yatube_api.models Post."""
    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'pub_date')


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели yatube_api.models Group."""
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели yatube_api.models Comment."""
    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'post', 'created')
