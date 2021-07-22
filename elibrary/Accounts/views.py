from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from django.http import HttpResponse
from ReadBook.models import UserInfo

# Create your views here.
def register_user(request):
	if not request.user.is_authenticated:
		if request.method=="POST":
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			username = request.POST['username']
			email = request.POST['email']
			user_type = request.POST['user_type']
			password1 = request.POST['password1']
			password2 = request.POST['password2']

			if password1 == password2:
				if User.objects.filter(username=username).exists():
					messages.info(request, 'username is taken, choose another!')
					return redirect('Accounts:register_user')

				elif User.objects.filter(email=email).exists():
					messages.info(request, 'Email is taken, choose another!')
					return redirect('Accounts:register_user')

				else:
					user = User.objects.create_user(username=username, password=password1,
						email=email, first_name=first_name, last_name=last_name)
					user.save()
					UserInfo.objects.create(id=user.id, 
						user_type=user_type, users_id = user.id)


					return redirect('Accounts:login_user')

			else:
				messages.info(request, 'Password didn\'t match')
				return redirect('Accounts:register_user')

		return render(request, 'Accounts/register.html')



def login_user(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']

			user = auth.authenticate(username=username, password=password) # checks db for user
			if user is not None:
				auth.login(request, user)
				return redirect('/')

			else:
				messages.info(request, 'invalid credentials!')
				return redirect('Accounts:login_user')

		else:
			return render(request, 'Accounts/login.html')

	else:
		return HttpResponse('you are not permitted to view this page!')

def logout_user(request):
	auth.logout(request)
	return redirect("Accounts:login_user")



