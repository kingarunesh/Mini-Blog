from django.shortcuts import render

from dashboard.forms import SignUpForm



#SECTION :      sign up

def sign_up(request):
    
    form = SignUpForm()
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="dashboard/sign-up.html", context=context)