from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    return render(request,'blog/post_list.html',{'posts':Post.objects.filter(published_date__lte = timezone.now()).order_by('title')})


def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if  form.is_valid():
            post = form.save(commit= False)
            post.author = request.user
            # this line is empty because here was the post.published_date line which we have removed so that we can save the post as drafts.
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
        return render(request,'blog/post_new.html',{'form':form})

def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST,instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            # this line is empty because here was the post.published_date line which we have removed so that we can save the post as drafts.
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm(instance = post)
        return render(request,'blog/post_new.html',{'form':form})

def draft_list(request):
    posts = Post.objects.filter(published_date__isnull = True).order_by('start_date')
    return render(request,'blog/draft_list',{'posts':posts})

def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return redirect('post_detail',pk=pk)
