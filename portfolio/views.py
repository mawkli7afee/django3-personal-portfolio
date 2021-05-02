from django.core.mail import send_mail
from .forms import ContactForm
from .models import Project
from django.contrib import messages
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

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            name = request.POST['full_name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']

            send_mail(
                name,
                message,
                email,
                ['mawkli_7afee@hotmail.com'],
            )

            return render(request, 'portfolio/contact.html', {'message': message})
        else:
            return render(request, 'portfolio/contact.html')
