from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Books
from .forms import BooksForm
# Create your views here.


def landing_page(request):
    return render(request, 'landing_page.html')


class Info(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'info.html')

    def post(self):
        pass#2024-05-23T12:21:01.686Z


def list_view(request):
    books = Books.objects.all().order_by('-date')
    return render(request, 'list_view.html', {'books': books})

def detail(request, pk):
    book = Books.objects.get(pk=pk)
    return render(request, 'detail.html', {'book': book})


def create(request):
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = BooksForm()
    return render(request, 'create.html', {'form': form})

def update_view(self, request, pk):
    book = Books.objects.get(pk=pk)
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = BooksForm(instance=book)
    return render(request, 'update_view.html', {'form': form})

def delete_view(self, request, pk):
    book = Books.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list')
    return render(request, 'delete_view.html', {'book': book})


