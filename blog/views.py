from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from blog.models import *

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    # posts = Post.objects.filter(status=1)
    # post = get_object_or_404(posts,pk = pid)

    post = get_object_or_404(Post,pk = pid, status = 1)
    context = {'post' : post}
    return render(request, 'blog/blog-single.html', context)