from django.shortcuts import render,redirect
from .models import *
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import BookSerializer

# Create your views here.
# Admin Signup View
def admin_signup(request):
    if (request.method=="POST"):
        if request.POST["name"]!="" and request.POST["email"]!="" and request.POST["pass"]!='' :
            if request.POST["pass"]:
                obj=Admin_Singup.objects.create(Name=request.POST['name'],Email=request.POST["email"],Password=request.POST["pass"])
                obj.save()
                return redirect("admin_login.1")
    return render(request,"admin_signup.html",{})

# Admin Login View
def admin_login(request):
    if request.method=="POST":
        if request.POST["email"]!="" and request.POST["password"]!="":
            admin_data=Admin_Singup.objects.all()
            for i in admin_data:
                print(i.Email)
                if i.Email==request.POST["email"] and i.Password==request.POST["password"]:
                    return redirect("book_data")
    return render(request,"admin_login.html",{})

# Books Data View
def books_data(request):
    count=0
    books=Books.objects.all()
    for i in books:
        count+=1
    print(books)
    return render(request,"books_data.html",{"books":books,"count":count})

# New Book Entery
def book_entry(request):
    if request.method=="POST":
        if request.POST["book_name"]!='' and request.POST.get('book_branch', False)!='' and request.POST["no_of_pages"]!='':
            books_data=Books.objects.all()
            for i in books_data:
                if i.Book_name==request.POST["book_name"]:
                    msg1="Book alerdy present..."
                    return render(request,"books_entry.html",{"msg1":msg1})
            book=Books.objects.create(Book_name=request.POST["book_name"],Branch=request.POST.get('book_branch', False),No_of_books=request.POST["no_of_pages"])
            book.save()
            msg="Succes fully added.."
            return render(request,"books_entry.html",{"msg":msg})
    return render(request,"books_entry.html",{})

# Update Book data
def book_update(request, id):
    emp = Books.objects.get(id = id)
    if request.method=="POST":
        emp.Book_name=request.POST.get('book_name')
        emp.Branch=request.POST.get("branch")
        emp.No_of_books=request.POST.get('no_books')
        print(request.POST.get('no_books'))
        emp.save()
        return redirect("book_data")
    return render(request,"update_book_details.html",{"data":emp})

# Delete Book data
def book_delete(request, id):
   emp = Books.objects.get(id = id)
   emp.delete()
   return render(request,"books_data.html",{})

# Get books list views Students 
def booklist(request):
    count=0
    books=Books.objects.all()
    for i in books:
        count+=1
    print(books)
    return render(request,"books_list.html",{"books":books,"count":count})


# Create your views here.
class ListBookAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class CreateBookAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class UpdateBookAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class DeleteBookAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Books.objects.all()
    serializer_class = BookSerializer