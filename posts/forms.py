from django import forms
from .models import Post, Subderppit, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'subderppit']
        
class SubderppitForm(forms.ModelForm):
    class Meta:
        model = Subderppit
        fields = ['name', 'title', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']