from django.shortcuts import render, get_object_or_404
from django.db.models import Count

from .models import Post, Author


def post_list(request):
    posts = Post.objects.all()
    latest_posts = Post.objects.order_by("-publish")[:4]
    context = {
        "posts": posts,
        "latest_posts": latest_posts,
    }
    return render(request, "blog/blog.html", context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post, slug=post, publish__year=year, publish__month=month, publish__day=day,
    )
    post_tags_ids = post.tags.values_list("id", flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by(
        "-same_tags", "-publish"
    )
    latest_posts = Post.objects.order_by("-publish")[:4]
    context = {
        "post": post,
        "similar_posts": similar_posts,
        "latest_posts": latest_posts,
    }

    return render(request, "blog/blog_detail.html", context)
