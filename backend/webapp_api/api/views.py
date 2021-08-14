from django.shortcuts import render
from rest_auth.views import LoginView, UserDetailsView
from rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
from rest_framework.permissions import IsAuthenticated
from rest_auth.views import PasswordResetConfirmView, PasswordResetView
from users.forms import ResetPasswordForm


#Overriding Login View
class CustomLoginView(LoginView):
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"message": "User Authenticated", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response

#Overridding Register View
class CustomRegisterView(RegisterView):
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"message": "User Created", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response

#Overridding UserDetail View
class CustomUserDetailsView(UserDetailsView):
    permission_classes = (IsAuthenticated,)
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"message": "User Details", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response

#Overridding VerifyEmail View
class CustomVerifyEmailView(VerifyEmailView):
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"message": "Email Sent", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response

#Overridding VerifyEmail View
class CustomConfirmEmailView(ConfirmEmailView):
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"message": "Email Verified", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response

class CustomPasswordResetView(PasswordResetView):
    form_class = ResetPasswordForm
         

    