
from django.http import HttpResponse
from .models import UserInfo

def author_only(func): # func is the function that the decorator is called on
	def wrapper(request, *args, **kwargs):
		if UserInfo.objects.filter(pk = request.user.id, user_type = "Author").exists():
			return func(request, *args, **kwargs)

		else:
			return HttpResponse("You have no permission to access this, Please sign up as Author!")
	return wrapper