from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import Serializer_user, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt
# Create your views here.


class Registration(GenericAPIView):
    serializer_class = Serializer_user
    # http_method_names = ['get', 'head', 'post']

    def post(self, request):
        serializer = Serializer_user(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username}, settings.SECRET_KEY_JWT, algorithm="HS256")

            serializer = Serializer_user(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
# class Login(GenericAPIView):

#     def post(self, request):
#         # the request gets us the users data
#         username = request.data('username', '')
#         password = request.data('password', '')
#         check_user = auth.authenticate(username=username, password=password)
#         if check_user:
#             auth_token = jwt.encode(
#                 {'username': check_user.username}, settings.SECRET_KEY_JWT, algorithm="HS256")
#             serializer = Serializer_user(check_user)
#             data = {'user': serializer.data, 'token': auth_token}

#             return Response(data, status=status.HTTP_200_OK)
#         return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
