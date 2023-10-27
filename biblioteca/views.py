from django.shortcuts import render, redirect
from .models import Books, Genres
from random import randint
from datetime import datetime

def index(request):

    books = Books.objects.all().order_by("cod")
    for book in books:
        print(f"book.name + book.gender")

    return render(request, "pages/index.html", {"books": books})

    gender = models.ForeignKey(Genres, on_delete=models.CASCADE)
    book_cover = models.ImageField(blank=False)
    author = models.CharField(max_length=255)
    pages = models.IntegerField()
    qtd = models.IntegerField()
    in_stock = models.BooleanField(default=False)


def add_books(request):
    if request.method == "POST":
        name = request.POST.get("name")
        unique_cod = False
        while not unique_cod:
            cod = randint(100, 10000)
            if not Books.objects.filter(cod=cod).exists():
                unique_cod = True

        gender = request.POST["gender"]
        book_cover = request.FILES.get("book_cover")
        author = request.POST["author"]
        description = request.POST.get("description")
        pages = request.POST["pages"]
        qtd = request.POST["qtd"]
        in_stock = True
        if int(qtd) == 0:
            in_stock = False


        Books.objects.create(

            cod=cod,
            name=name,
            gender_id=gender,
            picture=picture,
            author=author,
            pages=pages,
            qtd=qtd,
            in_stock=in_stock,
        )
        return redirect("home")
    else:
        categories = Genres.objects.all()
        return render(request, "pages/add_books.html", {"genres": genres})

def book_detail(request, id):
    book = Books.objects.get(id=id)
    return render(request, "pages/book_detail.html", {"book": book})

def delete_book(request, id):
    product = Books.objects.get(id=id).delete()
    return redirect("home")