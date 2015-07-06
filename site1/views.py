from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from site1.models import Post,Comment
from site1.forms import PostForm,MyRegistrationForm,CommentForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte= timezone.now()).order_by('-published_date')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request,pk):
     Post.objects.get(pk=pk)
     post = get_object_or_404(Post, pk=pk)
     print post
     return render(request,'post_detail.html',{'post':post})

def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.POST:
        form = PostForm(request.POST, instance=post)
        print request.POST
        print form.errors
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('site1.views.post_detail',pk=post.pk)
    else:
        form = PostForm(instance=post)
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

def add_comment(request,pk):
    post= get_object_or_404(Post,pk=pk)
    if request.POST:
        form = CommentForm(request.POST)
        print request.POST
        print form.errors
        if form.is_valid():
            comment= form.save(commit=False)
            comment.post= post
            comment.post()
            return redirect(request,'site1.views.post_detail',pk=post.pk)
        else:
            form= CommentForm()
        return render(request,'add_comment.html',{'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('site1.views.post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('site1.views.post_detail', pk=post_pk)
# Create your views here.
