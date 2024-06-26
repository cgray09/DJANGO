from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Customer(models.Model):
	# user from django so we can associate every customer w/ a user or the logged in user
	user = models.OneToOneField(User, null=True, on_delete =models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Outdoor', 'Outdoor'),
		)
	name = models.CharField(max_length=20, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices = CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name


class Order(models.Model):
	STATUS = (
			("Pending", "Pending" ),
			("Out for Delivery", "Out for Delivery"),
			("Delivered", "Delivered"),
		)
	# "on_delete=models.SET_NULL" is when customer is null the "customer" column is null
	customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=200, null=True)


	def __str__(self):
		return self.product.name



