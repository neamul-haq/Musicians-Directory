from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    # path('register/', views.register, name='register'),
    path('register/', views.registerView.as_view(), name='register'),
    # path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('logout/', views.user_logout, name='user_logout'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
]