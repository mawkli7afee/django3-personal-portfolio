"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from portfolio import views
from portfolio.views import HomeView, ContactUs, AddBook, AddPublisher, DetailBooks, AllBooks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactUs.as_view(), name='contact'),
    path('addpublisher/', AddPublisher.as_view(), name='addpublisher'),
    path('addbook/', AddBook.as_view(), name='addbook'),
    path('blog/', include('blog.urls')),
    path('all_books/', AllBooks.as_view(), name="all_books"),
    path('<int:pk>/', DetailBooks.as_view(), name='detailbooks'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
