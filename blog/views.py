from django.shortcuts import render, HttpResponse
from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request,'blog/blogIndex.html', {'blogs': blogs})

def blogPost(request,id):
    # return HttpResponse(id)
    blog = Blog.objects.filter(blog_id=id)[0]
    return render(request, 'blog/blogPost.html', {'blog':blog})
