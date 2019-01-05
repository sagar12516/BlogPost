from django.urls import path,include
from .views import register,profile
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('register/',register,name='user-register'),
    path('profile/',profile,name='user-profile'),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'),name='user-login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='user-logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete')
]
