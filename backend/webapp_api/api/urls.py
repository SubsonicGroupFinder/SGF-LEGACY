# api/urls.py
from django.urls import include, path
from django.conf.urls import url
from api.views import CustomLoginView, CustomRegisterView, CustomUserDetailsView

urlpatterns = [
    path(r'custom/login/', CustomLoginView.as_view(), name='my_custom_login'),
    path(r'custom/register/', CustomRegisterView.as_view(), name='my_custom_register'),
    path(r'custom/user/', CustomUserDetailsView.as_view(), name='my_custom_user'),
    url(r'custom/', include('rest_auth.urls')),
]