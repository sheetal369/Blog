from django.urls import path
from apis.views import PostAPIView

app_name = "apis"

urlpatterns = [
    path("",  PostAPIView.as_view(), name="post_list" ),
]