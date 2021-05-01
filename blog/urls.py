
from django.urls import path, include

from blog.views import AllBlogs, DetailBlog

app_name = 'blog'

urlpatterns = [
    path('', AllBlogs.as_view(), name='all_blogs'),
    path('<int:pk>/', DetailBlog.as_view(), name='detail'),
]