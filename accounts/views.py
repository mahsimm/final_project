from django.shortcuts import render, redirect
from django.contrib import auth
from accounts.models import *
from accounts.serializers import *
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import exceptions
from django.contrib.auth.hashers import make_password
from django.urls import reverse


@permission_classes((AllowAny,))
class SignUp(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'accounts/signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('shop')
        return Response()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return render(request, 'accounts/signin.html', {'success': 'ثبت نام با موفقیت انجام شد.'})


@permission_classes((AllowAny,))
class SignIn(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'accounts/signin.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('shop')
        return Response()

    def post(self, request):
        username = request.data['username'].lower()
        user = auth.authenticate(
            username=username, password=request.data['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('shop')
        else:
            return Response({'error': 'نام کاربری یا رمز عبور اشتباه است'})


def main_page(request):
    if request.user.is_authenticated:
        return redirect('shop')
    else:
        return redirect('signin')

class SignOut(APIView):
    def get(self, request):
        auth.logout(request)
        return redirect('signin')
