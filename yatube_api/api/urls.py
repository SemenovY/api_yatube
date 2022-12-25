"""Навигация и роутеры."""
from rest_framework.routers import SimpleRouter
from django.urls import include, path
from rest_framework.authtoken import views
from .views import PostViewSet, CommentViewSet, GroupViewSet, UserViewSet

app_name = 'api'


router = SimpleRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comment',
                ),
router.register('users', UserViewSet)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls), name='api-root'),
]
