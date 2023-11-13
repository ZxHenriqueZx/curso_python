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

def post(request, post_id):
    post_single = None

    for post in posts:
        if post['id'] == post_id:
            post_single = post
            break

    context = {
        'post': post_single,
        'title': post_single['title'],
    }

    return render(
        request,
        'blog/post.html',
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

