from django.shortcuts import render, redirect
from .models import Book

from .decorators import author_only
from django.contrib.auth.decorators import login_required
# Create your views here.

def loadBook(request):
	books = Book.objects.all()
	return render(request, "ReadBook/Book.html", context={"books": books})
	
@login_required(login_url='/login/')
@author_only
def addBook(request):
	name = ''
	price = ''
	btype = ''
	cover = ''
	pdf = ''
	description = ''
	category = ''
	userid = ''


	if request.method == "POST":

		try:
			name = request.POST['name'].strip()
			btype = request.POST['type'].strip()
			description = request.POST['description']
			category = request.POST['category']
			cover = request.FILES.get('image', None)
			pdf = request.FILES.get('files')
			userid = request.user.id


			if btype != 'Free':
				price = int(request.POST['price'])
			else:
				price = 0

			Book.objects.create(book_name=name, book_price=price, book_type=btype,
				book_cover = cover, book_description = description, 
				book_category = category, book_file = pdf, uploaded_by_id=userid)

			return redirect('ReadBook:premiumbook')

		except Exception as e:
			print("Error: "+ str(e))



	return render(request, "ReadBook/AddBook.html", context={

		"bookname": name,
		"bookprice" : price,
		"description": description,
		"category": category

		})


def bookDescription(request, bid):

	book = None
	owner = False
	loggedin = True if request.user.is_authenticated else False

	if Book.objects.filter(id=bid).exists():
		try:
			book = Book.objects.get(id=bid)
			if loggedin:
				owner = True if Book.objects.get(pk= bid).uploaded_by_id == request.user.id else False

		except Exception as e:
			print(str(e))
	else:
		return redirect("ReadBook:premiumbook")

	return render(request, "ReadBook/BookDescription.html", context={

		'book' : book,
		'loggedin': loggedin,
		'owner': owner

		})

# he never gave a button for this method in the app so if you want to use it you have
# to call it manually through the url
@login_required(login_url='/login/')
@author_only
def deleteBook(request, bid):
	book = None
	if Book.objects.filter(id=bid).exists():
		book = Book.objects.get(id=bid)
		book.delete()
	return redirect('ReadBook:premiumbook')
