from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_page, name="login"),
    path("register/", views.register_page, name="register"),
    # path("home/", views.home, name="home"),
    path("logout/", views.logout_user, name="logout"),
    path("create_user/", views.create_user, name="create_user"),
    path("admin_panel/", views.admin_panel, name="admin_panel"),
]
