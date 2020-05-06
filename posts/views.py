from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from posts.models import Post
from posts.forms import PostForm, PostModelForm
from django.db.models import Q
# Create your views here.


def posts_list(request):
    if request.method == 'POST':
        search_query = request.POST.get('search')
        # posts_matched_title = Post.objects.filter(
        #     title__icontains=search_query)
        # posts_matched_content = Post.objects.filter(
        #     content__icontains=search_query)
        # posts_matched = posts_matched_title | posts_matched_content
        posts = Post.objects.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query))
    else:
        search_query = ''
        posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {"posts": posts, "search": search_query})


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
