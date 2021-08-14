# api/urls.py
from django.urls import include, path
from django.conf.urls import url
from api.views import CustomLoginView, CustomRegisterView, CustomUserDetailsView, CustomPasswordResetView
from rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from rest_auth.views import PasswordResetConfirmView


urlpatterns = [
    url('', include('rest_auth.urls')),
    url(r'^password/reset/$', CustomPasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/<slug:uidb64>/<slug:token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('register/account-confirm-email/<str:key>/', ConfirmEmailView.as_view(),),
    path('register/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('login/', CustomLoginView.as_view(), name='my_custom_login'),
    path('register/', include('rest_auth.registration.urls')),
    path('register/', CustomRegisterView.as_view(), name='my_custom_register'),
    path('user/', CustomUserDetailsView.as_view(), name='my_custom_user'),   
]
