from django.template.response import TemplateResponse
from .models import Book


def books(request):
    return TemplateResponse(
        request,
        "books/books.html",
        {"books": Book.objects.all()},
    )
