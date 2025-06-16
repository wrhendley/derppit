from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView
from django.views import View
from django.urls import reverse_lazy
from .models import Post, Subderppit, Comment
from .forms import PostForm, SubderppitForm, CommentForm

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comments.all().order_by('-created_at')
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            parent_id = request.POST.get('parent_comment_id')
            if parent_id:
                comment.parent_comment_id = parent_id
            comment.save()
            return redirect('post_detail', pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))

class ReplyToCommentView(View):
    def post(self, request, pk, parent_id):
        post = get_object_or_404(Post, pk=pk)
        parent_comment = get_object_or_404(Comment, pk=parent_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.post = post
            reply.parent = parent_comment
            reply.save()
        return redirect('post_detail', pk=pk)