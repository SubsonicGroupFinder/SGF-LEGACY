from django.shortcuts import render
from rest_auth.views import LoginView 
from rest_auth.registration.views import RegisterView
from rest_framework import generics

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

    