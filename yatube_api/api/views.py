"""Viewset для работы с моделями."""
from rest_framework import viewsets
from .serializers import PostSerializer#, CommentSerializer, GroupSerializer
from posts.models import Post#, Comment, Group


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """Вьюсет для модели Group."""
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#
#
# class CommentViewSet(viewsets.ModelViewSet):
#     """Вьюсет для модели Comment."""
#     serializer_class = CommentSerializer
#
#     def get_queryset(self):
#         post_id = self.kwargs.get('post_id')
#         new_queryset = Post.objects.filter(post=post_id)
#         return new_queryset
