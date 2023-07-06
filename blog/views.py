from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Post
from django.http import request
from django.urls import reverse
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    queryset = Post.published.all()
    template_name = "blog/post/list.html"
    context_object_name = "posts"

# def post_list(request):
#     posts = Post.published.all()
#     return render(request, "blog/post/list.html", {"posts": posts})

# def post_detail(request, year, month, day, post):
#     post = get_object_or_404(
#         Post,
#         status=Post.Status.PUBLISHED,
#         slug=post,
#         publish__year=year,
#         publish__month=month,
#         publish__day=day,
#     )
    
#     return render(request, "blog/post/detail.html", {"post": post})


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post/detail.html"
    context_object_name = "post"
    slug_url_kwarg = "post"
    year_url_kwarg = "year"
    month_url_kwarg = "month"
    day_url_kwarg = "day"
    queryset = Post.objects.filter(status=Post.Status.PUBLISHED)

    def get_object(self, queryset=None):
        year = self.kwargs.get("year")
        month = self.kwargs.get("month")
        day = self.kwargs.get("day")
        slug = self.kwargs.get("post")
        queryset = self.get_queryset()
        
        return get_object_or_404(
            queryset,
            publish__year=year,
            publish__month=month,
            publish__day=day,
            slug=slug,
        )

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        # import ipdb ; ipdb.set_trace() - used for testing
        if form.is_valid():
            form.save()
            return redirect(reverse("core:my_blogs"))
            # Redirect or perform any other action upon successful form submission

    else:
        form = PostForm()
    return render(request, "blog/post/create_post.html", {"form": form})

@login_required
def delete_post(request):
    if request.method == "POST":
        post_id = request.POST.get("id")
        Post.objects.filter(id=post_id).delete()
    return redirect(reverse("core:my_blogs"))

@login_required
def edit_post(request):
    post_id = request.GET.get("id")
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse("core:my_blogs"))
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post/edit_post.html", {"form": form})
