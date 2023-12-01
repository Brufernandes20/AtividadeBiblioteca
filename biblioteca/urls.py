from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("search-book/", views.search_book, name="search-book"),
    path("stockless/", views.stockless, name="stockless"),
    path("add-book/", views.add_book, name="add-book"),
    path("delete-book/<int:id>/", views.delete_book, name="delete-book"),
    path("sell-book/<int:id>/", views.sell_book, name="sell-book"),
    path("book-detail/<int:id>/", views.book_detail, name="book-detail"),
    path("return-book/<int:id>/", views.return_book, name="return-book"),
]