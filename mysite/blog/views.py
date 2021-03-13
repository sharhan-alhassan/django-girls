from django.shortcuts import render

# Create your views here.

def index(request):
    context = "<h1>Hello</h1>"
    return render(request, 'blog/index.html', {'context':context})