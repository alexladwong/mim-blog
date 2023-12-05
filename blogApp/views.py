from django.shortcuts import redirect, render
from .forms import CommentForm
from .models import Post


# Create your views here.
def frontpage(request):
    posts = Post.objects.all()
    return render(request, "blogApp/frontpage.html", {"posts": posts})


def post_details(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect("post_details", slug=post.slug)

    else:
        form = CommentForm()

    return render(request, "blogApp/post_details.html", {"post": post, "form": form})
