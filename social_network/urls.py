from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name = "home"),
    path('home', views.home_view, name = "home"),
    path('sign-up/', views.sign_up_view, name = "sign_up"),
    path('create-post/', views.create_post_view, name = "create_post"),
]
