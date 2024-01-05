from datetime import datetime
from django.shortcuts import render



def index(request):
    year = datetime.now().year
    
    context = {
        "year": year
    }
    
    return render(request=request, template_name="index/index.html", context=context)