from django.urls import path
from .views import user_login, user_logout, profile_edit,multi_step_register, profile_view, verify_email, password_reset_request, password_reset_verify, password_reset_form
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', multi_step_register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile-edit/', profile_edit, name='profile_edit'),
    path('verify_email/<int:user_id>/', verify_email, name='verify_email'),
    path('password_reset/', password_reset_request, name='password_reset'),
    path('password_reset_verify/<int:user_id>/', password_reset_verify, name='password_reset_verify'),
    path('password_reset_form/<int:user_id>/', password_reset_form, name='password_reset_form'),
    path(
        'password_change/',
        login_required(PasswordChangeView.as_view(template_name='accounts/password_change_form.html')),
        name='password_change'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
        name='password_change_done'
    ),
]
