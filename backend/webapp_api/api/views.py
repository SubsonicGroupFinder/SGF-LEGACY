from django.shortcuts import render
from rest_auth.views import LoginView, UserDetailsView
from rest_auth.registration.views import RegisterView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


#Overriding Login View
class CustomLoginView(LoginView):
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"message": "User Authenticated", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response

class CustomRegisterView(RegisterView):
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"message": "User Created", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response

class CustomUserDetailsView(UserDetailsView):
    permission_classes = (IsAuthenticated,)
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"message": "User Details", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response
        
         

    