from django.shortcuts import render, redirect

from .models import ideapeacher

from django.http import HttpResponse
from django.contrib import messages
from .forms import CreateUserForm

from .decorators import *


from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group

from .models import idea, Public, category
from datetime import datetime
# Create your views here.


def registerPeacher(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

		if not Group.objects.filter(name="ideapeacher").exists():
			group = Group.objects.create(name="ideapeacher")
			addtogroup = Group.objects.get(name='ideapeacher')
			user.groups.add(addtogroup)

			ideapeacher.objects.create(user=user, name=user.username )
			messages.success(request, 'Account was created for '+ username)
			return HttpResponse("Created user with group ideapeacher")

		else:
			group = Group.objects.get(name='ideapeacher')
			user.groups.add(group)
			ideapeacher.objects.create(user=user, name=user.username )
			messages.success(request, 'Account was created for '+ username)
			return HttpResponse("Created user with group ideapeacher")

	context = {'form': form}

	return render(request, 'main/register.html', context)


def login_request(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return HttpResponse("Login successful")


		else:
			messages.info(request, 'Username or password is incorrect!')


	return render(request, "main/login.html")


def logout_request(request):
	logout(request)
	return redirect('login_request')



@ideapeacher_only
def ideapeacherpage(request):
	i = idea.objects.all()
	b = Public.objects.all()

	return render(request, "main/home.html", {"ideas":i, 'comments': b})



@allowed_users(allowed_roles=['sponser'])
def sponserPage(request):
	u = ideapeacher.objects.all()
	i = idea.objects.all()

	return render(request, "main/home1.html", {"ideas": i, "users": u})


@allowed_users(allowed_roles=['ideapeacher'])
def submitidea(request):
	if request.method == "POST":
		c = request.POST.get("dropdown")

		#logic what if category doesnot exist for that particular idea

		if not category.objects.filter(category=c).exists():
			rp = category(category=c)
			rp.save()


			i = request.POST.get("idea")
			u = ideapeacher.objects.get(user=request.user)
			p = request.FILES.get("pdf")

			d= datetime.now()

			post = idea(peacher=u, post_idea=i, date_created=d, pdf=p)
			post.save()
			post.category.add(rp)
			return redirect("/home")

		else:
			cp = category.objects.get(category=c)
			i = request.POST.get("idea")
			u = ideapeacher.objects.get(user=request.user)
			p = request.FILES.get("pdf")

			d= datetime.now()
			post = idea(peacher=u, post_idea=i, date_created=d, pdf=p)
			post.save()
			post.category.add(cp)


	return redirect("/home")





def post(request):
	return render(request, "main/idea.html")


def comment(request, pk):
	if request.method == "POST":
		f = idea.objects.get(pk=pk)
		i = request.POST.get("comment")

		u = request.user
		d = datetime.now()

		post = Public(comment=i, date_created=d, on_post=f, by=u)
		post.save()

	return redirect("home")

@allowed_users(allowed_roles=['ideapeacher'])
def edit_idea(request, pk):
	i = idea.objects.get(pk=pk)
	context = {
	'share': i
	}

	return render(request, "main/edit.html", context)


@allowed_users(allowed_roles=['ideapeacher'])
def updateidea(request,pk):
	i = idea.objects.get(pk=pk)
	i.post_idea = request.POST.get('idea')
	i.date_created = datetime.now()
	i.save()
	return redirect("home")

@allowed_users(allowed_roles=['ideapeacher'])
def delete(request, pk):
	i = idea.objects.get(pk=pk)
	i.delete()
	return redirect("home")