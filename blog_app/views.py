from django.shortcuts import render, redirect
from blog_app.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by("-published_at")
    return render(
        request,
        "post_list.html",
        {"posts": posts},
    )
    
def post_detail(request, pk):
    post = Post.objects.get(pk=pk, published_at__isnull=False)
    return render(
        request,
        "post_detail.html",
        {"post":post}
    )


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect("post-list")


@login_required
def draft_list(request):
    posts = Post.objects.filter(published_at__isnull=True)
    return render(
        request,
        "draft_list.html",
        {"posts": posts},
    )



def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    post.edit()
    return render(
        request,
        'post_edit.html',
        { 'post': post }
    )