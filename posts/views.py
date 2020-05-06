from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from posts.models import Post
from posts.forms import PostForm, PostModelForm
# Create your views here.


def posts_list(request):
    posts = Post.objects.all()
    # posts = Post.objects.published()
    return render(request, 'posts/post_list.html', {"posts": posts})


def posts_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post_detail.html', {"post": post})


@login_required()
def post_create(request):
    form = PostModelForm()
    # form = PostForm()
    if request.method == 'POST':
        # form = PostForm(request.POST)
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            print("Valid data")
            print(form.cleaned_data)
            # obj = Post.objects.create(**form.cleaned_data)
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('home')
    return render(request, 'posts/post_create.html', {"form": form, 'action_url': 'post_create'})


@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostModelForm(instance=post)
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'posts/post_create.html', {'form': form, 'action_url': 'post_update'})


@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('home')
