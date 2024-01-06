from django.shortcuts import render

from blog.models import Blog


def blog(request):
    
    context = {
        "blogs": Blog.objects.all()
    }
    
    return render(request=request, template_name="blog/blog.html", context=context)


def blog_details(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    
    context = {
        "blog": blog
    }
    
    return render(request=request, template_name="blog/blog-details.html", context=context)