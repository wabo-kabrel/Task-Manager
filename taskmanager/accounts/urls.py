from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    path('register/', register, name='register'),  # URL for user registration
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),  # URL for user login
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # URL for user logout
]