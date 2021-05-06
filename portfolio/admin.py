from django.contrib import admin
from .models import Project, Contact, Publisher, Book

admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(Publisher)
admin.site.register(Book)
