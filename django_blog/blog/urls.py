from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    # ...plus your auth views (register, profile, etc.) if they live here
)

urlpatterns = [
    path('', views.home, name='home'),                      # Home page
    path('posts/', views.post_list, name='posts'),          # Blog posts list
    path('register/', views.register, name='register'),     # Registration
    path('profile/', views.profile, name='profile'),        # Profile
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    path('post/', PostListView.as_view(), name='posts'),                # list
    path('post/new/', PostCreateView.as_view(), name='post-create'),    # create
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # detail
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # update
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # delete
]
