from django.urls import path

from .apps import UsersConfig
from users import views

app_name = UsersConfig.name

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', views.email_verification, name='email-confirm'),
    path('profile/<int:pk>/', views.UserUpdateView.as_view(), name='profile'),
    path('forgot-password/', views.UserForgotPasswordView.as_view(), name='forgot-password'),
    path('users-list/', views.UserListView.as_view(), name='users-list'),
    path('change-status/<int:pk>/', views.change_status, name='change-status'),
]
