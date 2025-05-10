from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('guest/<int:pk>/', views.guest_detail, name='guest_detail'),
    path('guests/', views.guest_list, name='guest_list'),  # Adjusted URL for guest list
    path('guest/<int:pk>/', views.guest_detail, name='guest_detail'),
    path('guest/create/', views.guest_create, name='guest_create'),
    path('guest/<int:pk>/edit/', views.guest_update, name='guest_update'),
    path('guest/<int:pk>/delete/', views.guest_delete, name='guest_delete'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
