from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from django.db.models import Q
from django.contrib import auth

from rest_framework.response import Response
from rest_framework import generics, parsers
from rest_framework import exceptions as rest_exceptions

from core.serializers import UserSerializer

class LoginView(generics.SingleObjectAPIView):
    '''
    Authentication!!!
    '''
    parser_classes = (parsers.JSONParser,)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return Response({})

        username = request.DATA.get('username')
        password = request.DATA.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)

            serializer = UserSerializer(user)
            return Response(serializer.data)
        raise rest_exceptions.NotAuthenticated('Authentication failed.')

class LogoutView(generics.SingleObjectAPIView):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return Response({})

class PingView(generics.SingleObjectAPIView):
    '''
    Ping. Pong.
    '''
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            raise rest_exceptions.NotAuthenticated('Not authenticated')
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class RegisterView(generics.SingleObjectAPIView):
    '''
    Register for an account.
    '''
    parser_classes = (parsers.JSONParser,)

    def post(self, request, *args, **kwargs):
        username = request.DATA.get('username')
        password = request.DATA.get('password')
        email = request.DATA.get('email')
        first_name = request.DATA.get('first_name')
        last_name = request.DATA.get('last_name')

        if not all((email,
                   username,
                   password)):
            raise rest_exceptions.ParseError('email, username, and password ' \
                                             'are required fields.')


        # TODO: Probbaly better validation here.
        try:
            user = User.objects.get(Q(username=username) | Q(email=email))

            # User with username or email already exists...bad.
            raise rest_exceptions.PermissionDenied('User already exists.')
        except User.DoesNotExist:
            # good!
            pass

        try:
            user = User.objects.create_user(username=username, 
                                            password=password,
                                            email=email)
        except IntegrityError:
            raise rest_exceptions.PermissionDenied('User already exists. BOO')

        if first_name:
            user.first_name = first_name

        if last_name:
            user.last_name = last_name
        
        user.save()

        g = Group.objects.get(name='BaseUsers') 
        g.user_set.add(user)

        g = Group.objects.get(name='PaidUsers') 
        g.user_set.add(user)

        serializer = UserSerializer(user)
        return Response(serializer.data)
