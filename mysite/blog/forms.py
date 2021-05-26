from django import forms
from django.db.models import fields
from . models import Comment, Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ['author', 'published_date']


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'text',)