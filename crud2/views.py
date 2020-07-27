from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from .models import Post
from .forms import PostForm


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()

    return render(request, 'crud2/post_form.html', {
        'form': form,
    })


def post_list(request):
    qs = Post.objects.all()  # QuerySet
    return render(request, 'crud2/post_list.html', {
        'post_list': qs,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'crud2/post_detail.html', {
        'post': post,
    })
