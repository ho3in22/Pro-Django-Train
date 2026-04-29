from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import *
from blog.forms import *
from django.contrib import messages


# Create your views here.
def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None :
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None :
        posts = posts.filter(tag__name__in = [kwargs['tag_name']])
        # posts = posts.filter(tag__name=kwargs['tag_name']) # behtare choon yeki hast

    posts = Paginator(posts, 2)
    try :
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger :
        posts = posts.get_page(1)
    except EmptyPage :
        posts = posts.get_page(posts.num_pages)
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)

# def blog_view(request, cat_name=None, author_username=None):
    # if cat_name != None :
    #     posts = posts.filter(category__name = cat_name)
    # if author_username != None:
    #     posts = posts.filter(author__username = author_username)

def blog_single(request, pid):
    # posts = Post.objects.filter(status=1)
    # post = get_object_or_404(posts,pk = pid)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your Comment added !')
        else :
            messages.add_message(request, messages.ERROR, 'Your Comment DID NOT added !')
    
    post = get_object_or_404(Post,pk = pid, status = 1)
    if not post.login_require :
        comments = Comment.objects.filter(post=post.id, approved=True) #.order_by('-created_date')    added in model Meta class
        form = CommentForm()
        context = {'post' : post, 'comments' : comments, 'form' : form}
        return render(request, 'blog/blog-single.html', context)
    else :
        return redirect('accounts:login')

# def blog_category(request, cat_name):
#     posts = Post.objects.filter(status=1)
#     posts = posts.filter(category__name = cat_name)

#     context = {'posts' : posts}
#     return render(request, 'blog/blog-home.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == "GET":
        if s := request.GET.get('s') :
            posts = posts.filter(content__contains = s)
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)