from django.shortcuts import render
from . models import Post
from django.utils import timezone

# Create your views here.

def index(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/index.html', {'post': post})