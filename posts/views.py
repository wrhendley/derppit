from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Post, Subderppit
from .forms import PostForm, SubderppitForm

def post_list(request):
    return render(request, 'posts/homepage.html')

def create_post(request):
    return render(request, 'posts/create_post.html')

def create_subderppit(request):
    return render(request, 'posts/create_subderppit.html')

@method_decorator(login_required, name='dispatch')
class CreateSubderppitView(CreateView):
    model = Subderppit
    form_class = SubderppitForm
    template_name = 'create_subderppit.html'
    success_url = reverse_lazy('post_list')

@method_decorator(login_required, name='dispatch')
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('post_list')
