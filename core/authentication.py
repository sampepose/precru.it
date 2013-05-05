from rest_framework import authentication
from rest_framework import exceptions

class BaseAuthentication(authentication.SessionAuthentication):

    def authenticate(self, request):
        user = super(BaseAuthentication, self).authenticate(request)
        if not user:
            raise exceptions.AuthenticationFailed('Not authenticated')

        request.user = user
        return user

