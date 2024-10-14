from django.shortcuts import render

# Django provides a shortcut to call get() on a given model manager
# and raises an Http404 exception instead of a
# DoesNotExist exception when no object is found
from django.shortcuts import get_object_or_404

from django.http import Http404

from .models import Post

# Create your views here.
def post_list(request): # this request parameter is required by all views
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

"""
def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post Found")
    return render(request, 'blog/post/detail.html', {'post': post})"""
# Both functions are correct
def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})
