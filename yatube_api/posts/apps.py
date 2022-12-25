"""Приложение Post."""
from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Создаем класс."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    verbose_name = 'Управление постами проекта'
