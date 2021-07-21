from django.shortcuts import render, redirect

# Create your views here.

from .forms import CreateUserForm, OrderForm
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout

from .models import Customer, Order
from .decorators import allowed_users, admin_only

def registerPage(request):
	form = CreateUserForm()
	if request.method == "POST":
		form = CreateUserForm(request.POST) # "request.POST" gets the data coming from the post (register.html)
		if form.is_valid()
			user = form.save()c
			username = form.cleaned_data.get("username")

			# creates and saves in the db
			Customer.objects.create(user = user, name=user.username)

			return redirect('login')

			messages.success(request, 'Account was created for ' + username)

	return render(request, "accounts/register.html", {'form': form})



def loginPage(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(request, username = username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')

		else:
			messages.info(request, "Username or password is incorrect!")


	return render(request, "accounts/login.html", {})



def logoutUser(request):
	logout(request)
	return redirect("login")

@admin_only
def home(request):
	orders = Order.objects.all()	# get all orders in db
	customers = Customer.objects.all()

	total_customers = customers.count()
	total_orders = orders.count()

	delivered = orders.filter(status="Delivered").count()
	pending = orders.filter(status="Pending").count()

	context = {'orders': orders, 'customers': customers,
				'total_orders': total_orders, 'delivered': delivered,
				'pending' : pending
	}

	return render(request, "accounts/dashboard.html", context)


@allowed_users(allowed_roles=['customer']) # from decorators.py
def userPage(request):	
	# can get orders since Customer is a foriegn key on Order
	orders = request.user.customer.order_set.all() #orders object of particular customer
	total_orders = orders.count()
	delivered = orders.filter(status="delivered").count()
	pending = orders.filter(status="pending").count()

	context = {'orders': orders, 'total_orders': total_orders,
				'delivered': delivered, 'pending': pending
					}

	return render(request, "accounts/user.html", context)



def updateOrder(request, pk):
	form = OrderForm()
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		form = OrderForm(request.POST, instance = order) # gives us the previously stored data in 
														 # the form
		if form.is_valid():
			form.save()
			return redirect("/")

	context = {'form': form}

	return render(request, "accounts/order_form.html", context)


def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')
#item.id ==> order.id
	context = {'item': order}

	return render(request, "accounts/delete.html", context)


