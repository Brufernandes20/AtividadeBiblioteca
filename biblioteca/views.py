from django.shortcuts import render, redirect
from .models import Books, Genres
from random import randint
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name="login")
def index(request):
    
    books = Books.objects.filter(user_id=request.user.id).order_by("cod")
    

    for book in books:
        print(f"book.nome + book.price")
    return render(request, "pages/index.html", {"books": books})


def stockless(request):
    books = Books.objects.filter(in_stock=False)
    return render(request, "pages/index.html", {"books": books})


def search_book(request):
    q = request.GET.get("q")
    if q == "":
        books = Books.objects.filter(name__icontains=q)
    else:
        books = Books.objects.filter(name__icontains=q).order_by("cod")
    return render(request, "pages/index.html", {"books": books})


def add_book(request):
    if request.method == "POST":
        name = request.POST.get("name")

        unique_cod = False
        while not unique_cod:
            cod = randint(100, 10000)
            if not Books.objects.filter(cod=cod).exists():
                unique_cod = True

        gender = request.POST.get("gender")
        # gender = Genres.objects.get(id=gender_id) if gender_id else None

        picture = request.FILES.get("imagem")
        author = request.POST.get("author")
        qtd = request.POST["qtd"]
        pages = request.POST["pages"]

        in_stock = True if int(qtd) > 0 else False

        Books.objects.create(
            user_id=request.user.id,
            name=name,
            cod=cod,
            gender_id=gender,
            picture=picture,
            author=author,
            qtd=qtd,
            pages=pages,
            in_stock=in_stock,
        )

        return redirect("home")
    else:
        genders = Genres.objects.all()
        return render(request, "pages/add_book.html", {"genders": genders})




def book_detail(request, id):
    book = Books.objects.get(id=id)
    return render(request, "pages/book_detail.html", {"book": book})


def delete_book(request, id):
    book = Books.objects.get(id=id).delete()
    return redirect("home")


def sell_book(request, id):
    book = Books.objects.get(id=id)
    if int(book.qtd) == 0:
        book.in_stock = False
        book.save()
        messages.success(request, "Este livro não possui estoque!")
    else:
        book.qtd -= 1
        book.save()
        messages.success(request, "Livro emprestado com sucesso!")
    return redirect("book-detail", id=id)

def return_book(request, id):
    book = Books.objects.get(id=id)
    book.qtd += 1
    book.save()
    messages.success(request, "Livro devolvido")
    return redirect("book-detail", id=id)