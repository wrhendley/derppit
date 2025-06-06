from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('posts/create/', views.create_post, name='create_post'),
    path('create_subderppit/', views.CreateSubderppitView.as_view(), name='create_subderppit'),
]
