from django.urls import path
from apis.views import *

app_name = "apis"

urlpatterns = [
    path("",  PostList.as_view(), name="post_list" ),
    path("<int:pk>", PostDetail.as_view(), name='post_detail')
]