from django.shortcuts import render
from .models import *
from .forms import * 


def index(request):
    
    if request.method == 'POST':
        add_book = BookForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()


    context = {
        'books':Book.objects.all(),
        'cat':Categ.objects.all(),
        'form': BookForm,
        }
    return render(request, 'pages/index.html',context)

def books(request):
       
    context = {   
        'cat':Categ.objects.all(),
        'books':Book.objects.all(),
        }
    return render(request,'pages/books.html',context)