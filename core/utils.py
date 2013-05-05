from django.contrib.auth.models import User

def is_authed(user, *args):
	if not user.is_authenticated():
        raise rest_exceptions.PermissionDenied()

    for arg in args:
	    if not user.has_perm("list_leads"):
        	raise rest_exceptions.PermissionDenied()
        	
    return True