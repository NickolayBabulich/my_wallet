from django.urls import path
from django.contrib.auth import views as auth_views

from apps.account import views

app_name = 'auth'

urlpatterns = [
    path('signin/', auth_views.LoginView.as_view(template_name='account/signin.html',
                                                 extra_context={'page_title': 'Аутентификация'}, ), name='signin'),

    path('signup/', views.SignUpView.as_view(extra_context={'page_title': 'Создание аккаунта'}), name='signup'),
    path('signup/done/', views.SignUpDoneView.as_view(extra_context={'page_title': 'Создание аккаунта'}),
         name='signup_done'),
    path('signup/confirm/', views.SignUpConfirmView.as_view(), name='signup_confirm'),
    path('verify/<uidb64>/<token>/', views.EmailVerificationView.as_view(), name='verify_email'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='account/password/password_reset_form.html',
             email_template_name='account/password/password_reset_email.html',
             html_email_template_name='account/password/password_reset_email.html',
             subject_template_name='account/password/password_reset_subject.txt',
             success_url='/auth/password-reset/done',
             extra_context={'page_title': 'Восстановление пароля'}
         ), name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='account/password/password_reset_done.html',
             extra_context={'page_title': 'Восстановление пароля'}
         ),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/password/password_reset_confirm.html',
             success_url='/auth/password-reset-complete/',
             extra_context={'page_title': 'Установка нового пароля'}
         ),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/password/password_reset_complete.html',
             extra_context={'page_title': 'Пароль изменен'}
         ),
         name='password_reset_complete'),

]
