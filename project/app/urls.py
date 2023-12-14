from django.urls import path

from .views import PostsView, create_view, delete_view, redact_view

urlpatterns = [
    path('create', create_view, name='create'),
    path('posts/all', PostsView, name='all'),
    path('delete/<int:id>', delete_view, name='delete'),
    path('update/<int:id>', redact_view, name='update')
]