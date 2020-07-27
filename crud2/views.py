from django.shortcuts import render
from .models import Post
from .forms import PostForm


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = PostForm()

    return render(request, 'crud2/post_form.html', {
        'form': form,
    })
