from django.contrib import messages
from django.urls import reverse_lazy

from .forms import ContactForm, AddBookForm, AddPublisherForm
from .models import Project, Book

from django.views.generic import ListView, FormView, DetailView
from django.shortcuts import render, redirect


# def home(request):
#     projects = Project.objects.all()
#     return render(request, 'portfolio/home.html', {'projects': projects})


class HomeView(ListView):
    template_name = 'portfolio/home.html'
    model = Project
    context_object_name = 'projects'


class ContactUs(FormView):
    form_class = ContactForm
    template_name = "portfolio/contact.html"
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, 'Thank You for Contacting us')
        return super().form_valid(form)


class AddPublisher(FormView):
    form_class = AddPublisherForm
    template_name = "portfolio/publisher.html"
    success_url = reverse_lazy('addbook')

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, 'New Author Added')
        return super().form_valid(form)


class AddBook(FormView):
    form_class = AddBookForm
    template_name = "portfolio/book.html"
    success_url = reverse_lazy('addbook')

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, 'New book Added')
        return super().form_valid(form)


class DetailBooks(DetailView):
    template_name = 'portfolio/book_detail.html'
    model = Book


class AllBooks(ListView):
    objects = Book.objects.all()
    template_name = 'portfolio/all_books.html'
    model = Book
    context_object_name = 'books'
