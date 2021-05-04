from django.contrib import messages
from .forms import ContactForm
from .models import Project

from django.views.generic import ListView, FormView
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
    success_url = "/contact/"

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, 'Thank You for Contacting us')
        return super().form_valid(form)
