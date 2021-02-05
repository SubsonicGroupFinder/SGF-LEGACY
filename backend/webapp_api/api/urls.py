# api/urls.py
from django.urls import include, path
from api.views import CustomLoginView, CustomRegisterView

urlpatterns = [
    path(r'custom/login/', CustomLoginView.as_view(), name='my_custom_register'),
    path(r'custom/register/', CustomRegisterView.as_view(), name='my_custom_register'),
]