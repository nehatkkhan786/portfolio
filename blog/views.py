from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def blog(request):
	blogs = Blog.objects.all()
	return render(request, 'blogs/blog.html', {'blogs': blogs})

	
def detail_blog(request, blog_id):
	blog = get_object_or_404(Blog, pk = blog_id)
	return render(request, 'blogs/detail_blog.html', {'blog_detail': blog})
