"""Libray URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from App1 import views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.booklist,name="bookslist"),
    path('admin_singup',views.admin_signup,name="admin_signup"),
    path("admin_login",views.admin_login,name="admin_login"),
    path("book_data",views.books_data,name="book_data"),
    path("book_entry",views.book_entry,name="book_entry"),
    path('update/<int:id>',views.book_update,name='book_update'),
    path('delete/<int:id>',views.book_delete,name="delete"),
    path("list",views.ListBookAPIView.as_view(),name="todo_list"),
    path("api_create_book/", views.CreateBookAPIView.as_view(),name="todo_create"),
    path("api_update_book/<int:pk>/",views.UpdateBookAPIView.as_view(),name="update_todo"),
    path("api_delete_book/<int:pk>/",views.DeleteBookAPIView.as_view(),name="delete_todo")
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)