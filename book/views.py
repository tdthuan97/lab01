from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book.models import Book


def index(request):
    request = "<h1>Hello World</h1>"
    return HttpResponse(request)

def showbook(request):
    lstbook = Book.objects.all()
    context = {'lstbook': lstbook}
    return render(request, 'listbook.html', context)

