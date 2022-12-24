from rest_framework import viewsets

from yatube_api.posts.models import Post
from yatube_api.api.serializers import PostSerializer

# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from . models import Post
# from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



# @api_view(['GET', 'POST'])
# def api_posts(request):
# 	if request.method == 'POST':
# 		serializer = PostSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save(author=request.user)
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# 	posts = Post.objects.all()
# 	serializer = PostSerializer(posts, many=True)
# 	return Response(serializer.data)


# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def api_posts_detail(request, pk):
# 	post = get_object_or_404(Post, id=pk)
#
# 	# напишем обработчик для метода GET
# 	if request.method == 'GET':
# 		serializer = PostSerializer(post)
# 		return Response(serializer.data, status=status.HTTP_200_OK)
#
# 	# получаем пользователя из запроса
# 	author = request.user
#
# 	# если пользователь, обратившийся к API, не является автором поста,
# 	# то к методам, идущим после GET, мы его не пропускаем
# 	# и возвращаем ответ со статусом 403
# 	if author == post.author:
# 		if request.method == 'PUT' or request.method == 'PATCH':
# 			serializer = PostSerializer(post, data=request.data, partial=True)
# 			if serializer.is_valid():
# 				serializer.save()
# 				return Response(serializer.data)
# 			return Response(serializer.errors,
# 							status=status.HTTP_400_BAD_REQUEST)
# 		elif request.method == 'DELETE':
# 			post.delete()
# 			return Response(status=status.HTTP_204_NO_CONTENT)
# 	else:
# 		return Response(status=status.HTTP_403_FORBIDDEN)
