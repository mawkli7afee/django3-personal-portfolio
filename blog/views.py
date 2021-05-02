from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views.generic import DetailView, ListView


# def all_blogs(request):
#     blogs = Blog.objects.order_by('-date')
#     return render(request, 'blog/all_blogs.html', {'blogs': blogs})
#
#
# def detail(request, blog_id):
#     blog = get_object_or_404(Blog, pk=blog_id)
#     return render(request, 'blog/detail.html', {'blog': blog})


class AllBlogs(ListView):
    objects = Blog.objects.all()
    template_name = 'blog/all_blogs.html'
    model = Blog
    context_object_name = 'blogs'


class DetailBlog(DetailView):
    template_name = 'blog/detail.html'
    model = Blog

