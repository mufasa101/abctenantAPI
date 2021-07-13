# from django.contrib import auth
# import jwt
# from rest_framework import authentication, exceptions
# from django.conf import settings
# from django.contrib.auth.models import User
import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth.models import User


class Authentication_jwt(authentication.BaseAuthentication):
    # def authenticate(self, request):
    #     auth_data = authentication.get_authorization_header(request)

    #     if not auth_data:
    #         return None

    #     prefix, token = auth_data.decode('utf-8').split(' ')

    #     try:
    #         payload = jwt.decode(
    #             token, settings.SECRET_KEY_JWT, algorithms="HS256")

    #         user = User.objects.get(username=payload['username'])
    #         return (user, token)

    #     except jwt.DecodeError as identifier:
    #         raise exceptions.AuthenticationFailed(
    #             'Your token is invalid,login')
    #     except jwt.ExpiredSignatureError as identifier:
    #         raise exceptions.AuthenticationFailed(
    #             'Your token is expired,login')

    #     return super().authenticate(request)
    def authenticate(self, request):
        data_sent = authentication.get_authorization_header(request)
        if not data_sent:
            return None
        prefix, token = data_sent.decode('utf-8').split(' ')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY_JWT, algorithms="HS256")
            user = User.objects.get(username=payload['username'])
            return(user, token)

        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is invalid,login')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is expired,login')
        return super().authenticate(request)
