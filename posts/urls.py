from django.urls import path
from .views import CreateSubderppitView, CreatePostView, post_list, PostDetailView, ReplyToCommentView

urlpatterns = [
    path('', post_list, name='post_list'),
    path('posts/create/', CreatePostView.as_view(), name='create_post'),
    path('posts/create_subderppit/', CreateSubderppitView.as_view(), name='create_subderppit'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/comments/<int:parent_id>/reply/', ReplyToCommentView.as_view(), name='reply_to_comment'),
]
