from django.shortcuts import render
from .models import *

def auther_list(request):
    authors = Author.objects.all()
    return render(request,'blog/author_list.htm',{'authors':authors})

def author_post(request,author_name):
    author = Author.objects.get(name=author_name)
    post = Post.objects.filter(author=author)
    return render(request,'blog/author_post.htm',{'post':post,'author':author_name})
def post_list(request):
    posts = Post.objects.all()
    context = {
        'post_list':posts
    }
    return render(request,'blog/post_list.htm',context)
def post_detail(request,post_id):
    post_detail = Post.objects.get(id=post_id)
    context ={
        'post_detail': post_detail
    }
    return render(request,'blog/post_detail.htm',context)
