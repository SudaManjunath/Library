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
    if request.method=="POST":
        books=Books.objects.all()
        return render(request,"books_data.html",{"books":books})

    return render(request,"books_data.html",{})
def admin_home(request):

    return render(request,"admin_home.html",{})
def book_entry(request):
    if request.method=="POST":
        book=Books.objects.create(Book_name=request.POST[""])
        msg="Succes fully added.."
        return render(request,"books_entry.html",{"msg":msg})
    return render(request,"books_entry.html",{})