from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def admin_signup(request):
    if (request.method=="POST"):
        if request.POST["name"]!="" and request.POST["email"]!="" and request.POST["pass"]!='' :
            if request.POST["pass"]:
                obj=Admin_Singup.objects.create(Name=request.POST['name'],Email=request.POST["email"],Password=request.POST["pass"])
                obj.save()
                return redirect("admin_login.1")
        
    return render(request,"admin_signup.html",{})
def admin_login(request):
    if request.method=="POST":
        if request.POST["email"]!="" and request.POST["password"]!="":
            admin_data=Admin_Singup.objects.all()
            for i in admin_data:
                print(i.Email)
                if i.Email==request.POST["email"] and i.Password==request.POST["password"]:
                    return redirect("book_data")
    return render(request,"admin_login.html",{})
def books_data(request):
    
    books=Books.objects.all()
    print(books)
    return render(request,"books_data.html",{"books":books})
def admin_home(request):

    return render(request,"admin_home.html",{})
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