from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>",
        views.PostDetailView.as_view(),
        name="post_detail",
    ),
    path("create/", views.create_post, name="create_post"),
    path("delete/", views.delete_post, name="delete_post"),
    path("edit/", views.edit_post, name="edit_post"),
]
