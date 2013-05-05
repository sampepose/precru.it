from django.contrib.auth.models import User
from rest_framework import exceptions as rest_exceptions

def is_authed(user, *args):
    if not user.is_authenticated():
        raise rest_exceptions.PermissionDenied()

    for arg in args:
        if not user.has_perm(arg):
            raise rest_exceptions.PermissionDenied()

    return True
