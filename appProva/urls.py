from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("page2/", views.page2, name="page2"),
    path("signUp/", views.register, name="register"),
    path("signIn/", views.login_user, name="login"),

]