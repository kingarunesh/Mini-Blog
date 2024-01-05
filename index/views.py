from datetime import datetime
from django.shortcuts import render

from blog.models import Blog


def index(request):
    year = datetime.now().year
    
    context = {
        "year": year,
        "blogs": Blog.objects.all()
    }
    
    return render(request=request, template_name="index/index.html", context=context)