from django.urls import path
from .views import CreateSubderppitView, CreatePostView, post_list

urlpatterns = [
    path('', post_list, name='post_list'),
    path('posts/create/', CreatePostView.as_view(), name='create_post'),
    path('posts/create_subderppit/', CreateSubderppitView.as_view(), name='create_subderppit'),
]
