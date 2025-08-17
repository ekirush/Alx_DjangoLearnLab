from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),                      # Home page
    path('posts/', views.post_list, name='posts'),          # Blog posts list
    path('register/', views.register, name='register'),     # Registration
    path('profile/', views.profile, name='profile'),        # Profile
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
]
