from django.shortcuts import render, HttpResponseRedirect

from blog.models import Blog
from blog.forms import BlogForm


#SECTION :      get all blogs
def blog(request):
    
    context = {
        "blogs": Blog.objects.all()
    }
    
    return render(request=request, template_name="blog/blog.html", context=context)



#SECTION :      blog details
def blog_details(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    
    context = {
        "blog": blog
    }
    
    return render(request=request, template_name="blog/blog-details.html", context=context)



#SECTION :      add new blog post
def add_blog(request):
    form = BlogForm()
    
    if request.method == "POST":
        form = BlogForm(request.POST)
        
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            
            data = Blog(title=title, description=description)
            data.save()
            
            return HttpResponseRedirect("/blog/")
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="blog/add-blog.html", context=context)



#SECTION :      delete blog

def delete_blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog.delete()
    
    return HttpResponseRedirect("/blog/")