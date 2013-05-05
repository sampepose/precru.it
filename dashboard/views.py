from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.contrib import messages, auth
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect


class IndexView(TemplateView):
    template_name = 'index.html'

class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            # Login
            auth.login(request, user)
            return redirect('landing-page')
        else:
            # Failed
            messages.error(request, 'Login was unsuccessful.  Please try again.')
            return redirect('landing-page')
        
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect('landing-page')
