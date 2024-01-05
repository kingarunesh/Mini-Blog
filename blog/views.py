from django.shortcuts import render

from blog.models import Blog


def blog(request):
    
    context = {
        "blogs": Blog.objects.all()
    }
    
    return render(request=request, template_name="blog/blog.html", context=context)