from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from . import api


app_name = "creator"

urlpatterns = [
    path("mypage/", views.mypage, name="mypage"),
    path("edit/", views.edit, name="edit"),
    
    path("creators/", views.creators, name="creators"),
    path("creators/<int:pk>", views.creator, name="creator"),
    path(
        "creators/<int:creator_id>/success/<int:support_id>/",
        views.support_success,
        name="success",
    ),
    
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="pages/creator/login.html"),
        name="login",
    ),
    path("signup/", views.signup, name="signup"),
    
    path("api/create_support/", api.create_support, name="api_create_support"),
]
