from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from site1.models import Post
from site1.forms import PostForm,MyRegistrationForm,Comment
from django.db import IntegrityError

def post_list(request):
    posts = Post.objects.filter(published_date__lte= timezone.now()).order_by('-published_date')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request,pk):
     Post.objects.get(pk=pk)
     post = get_object_or_404(Post, pk=pk)
     print post
     if request.POST:
         form= Comment(request.POST)
         if form.is_valid():
             comment = form.save(commit=False)
             comment.save()
             return redirect('site1.views.post_detail',pk=pk)
         else:
             post= Comment()
     return render(request,'post_detail.html',{'post':post})

def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('site1.views.post_detail', pk=post.pk)
    else:
            form = PostForm(instance=post)
            print form
            return render(request, 'post_edit.html', {'form':form})

def post_new(request):
    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('site1.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})

def registration(request):
    if request.POST:
        form = MyRegistrationForm(request.POST)
        print request.POST
        print form.errors
        if form.is_valid():
            form.save()
            return redirect('/site1/login/')
    else:
        form= MyRegistrationForm()
    return render(request,'registration.html',{'form':form})

def about_us(request):
    return render(request, 'about_us.html')

# Create your views here.
