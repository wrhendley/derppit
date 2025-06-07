from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .models import Post, Subderppit
from .forms import PostForm, SubderppitForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/homepage.html', {'posts': posts})

@method_decorator(login_required, name='dispatch')
class CreateSubderppitView(CreateView):
    model = Subderppit
    form_class = SubderppitForm
    template_name = 'posts/create_subderppit.html'
    success_url = reverse_lazy('post_list')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('post_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
