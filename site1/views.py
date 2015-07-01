from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from site1.models import Post
from site1.forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request,pk):
    Post.objects.get(pk=pk)

    post= get_object_or_404(Post, pk=pk)
    return render(request,'post_detail.html', {'post':post})

def post_new(request,pk):
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
    form = PostForm()
    print form
    return render(request, 'post_new.html', {'form':form})
# Create your views here.
