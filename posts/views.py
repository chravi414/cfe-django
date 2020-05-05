from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from posts.models import Post
from posts.forms import PostForm, PostModelForm
# Create your views here.


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {"posts": posts})


def posts_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post_detail.html', {"post": post})


def post_create(request):
    form = PostModelForm()
    # form = PostForm()
    if request.method == 'POST':
        # form = PostForm(request.POST)
        form = PostModelForm(request.POST)
        if form.is_valid():
            print("Valid data")
            print(form.cleaned_data)
            # obj = Post.objects.create(**form.cleaned_data)
            form.save()
    return render(request, 'posts/post_create.html', {"form": form})


def post_update(request, id):
    pass


def post_delete(request, id):
    pass
