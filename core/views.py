# Create your views here.

import peekedin.settings as settings
import oauth2
from core.models import UserProfile

consumer = oauth2.Consumer(settings.LINKEDIN_TOKEN, settings.LINKEDIN_SECRET)
client = oauth2.Client(consumer)
request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken'
access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
authenticate_url = 'https://www.linkedin.com/uas/oauth/authenticate'

def linkedin_login(request):
    pass

def linkedin_logout(request):
    pass

def linkedin_authenticated(request):
    pass
