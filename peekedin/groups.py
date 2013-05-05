from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

def init_groups():

	content_type = ContentType.objects.get_for_model(User)
	#Permissions
	has_paid = add_or_get_permission("Has paid", content_type, "has_paid")
	list_leads = add_or_get_permission("List leads", content_type, "list_leads")

	#Groups
	base_users, created = Group.objects.get_or_create(name='BaseUsers')
	base_users.save()

	paid_users, created = Group.objects.get_or_create(name='PaidUsers')
	paid_users.permissions = [has_paid, list_leads]
	paid_users.save()

def add_or_get_permission(name, content_type, codename):
	permission = Permission.objects.get(content_type=content_type, codename=codename)
	if permission is None:
		permission = Permission(name=name, content_type=content_type, codename=codename)
		permission.save()
	return permission