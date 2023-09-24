from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Ja',
        'title': 'Blog Post 1',
        'content': 'First post comment',
        'date_posted': 'August 27, 2023'
    },
    {
        'author': 'Ty',
        'title': 'Blog Post 2',
        'content': 'Second post comment',
        'date_posted': 'August 28, 2023'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
