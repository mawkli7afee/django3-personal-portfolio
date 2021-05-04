from django.db import models
from django.urls import reverse_lazy, reverse
from phonenumber_field.modelfields import PhoneNumberField


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False)
    phone = PhoneNumberField(null=False, blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.name

