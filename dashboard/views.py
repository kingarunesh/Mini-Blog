from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from dashboard.forms import SignUpForm



#SECTION :      dashboard

def dashboard(request):
    return render(request=request, template_name="dashboard/dashboard.html")




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


#SECTION :      login
def login_view(request):
    form = AuthenticationForm()
    
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(username=username, password=password)
            
            login(request=request, user=user)
            
            
            return HttpResponseRedirect("/dashboard/")
            
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="dashboard/login.html", context=context)






#SECTION :      logout

def logout_view(request):
    logout(request=request)
    
    return HttpResponseRedirect("/login/")