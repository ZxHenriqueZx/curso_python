from blog.data_posts import posts
from django.shortcuts import render

# Create your views here.
def blog(request):
    context = {
        #'text': 'Hello Blog!!',
        'title': 'Blog',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context,
    )

def exemplo(request):
    context = {
        'text': 'Hello Exemplo!!',
        'title': 'Exemplo',
    }

    return render(
        request,
        'blog/exemplo.html',
        context,
    )

