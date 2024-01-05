from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages

from contact.forms import ContactForm
from contact.models import Contact


def contact(request):
    
    form = ContactForm()
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(request=request, message="Your message sent.")
                        
            return HttpResponseRedirect("/contact/")
            
    context = {
        "form": form
    }
    
    return render(request=request, template_name="contact/contact.html", context=context)