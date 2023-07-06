from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path("",  PostListView.as_view(), name="post_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>",
         PostDetailView.as_view(),
        name="post_detail",
    ),
    path("create/",  create_post, name="create_post"),
    path("delete/",  delete_post, name="delete_post"),
    path("edit/",  edit_post, name="edit_post"),
]
