from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from dashboard.forms import SignUpForm



#SECTION :      dashboard

#NOTE :         dashboard
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login_view")
    
    context = {
        "user": request.user
    }
    
    return render(request=request, template_name="dashboard/dashboard.html", context=context)


#NOTE :         profile
def edit_profile_view(request):
    return render(request=request, template_name="dashboard/profile.html")


#NOTE :         change password
def change_password_view(request):
    return render(request=request, template_name="dashboard/change-password.html")


#NOTE :         blogs
def blogs_view(request):
    return render(request=request, template_name="dashboard/blogs.html")



#SECTION :      sign up
def sign_up(request):
    
    if request.user.is_authenticated:
        return redirect("dashboard")
    
    form = SignUpForm()
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            
            user = authenticate(username=username, password=password)
            login(request=request, user=user)
            
            return redirect("login_view")
            
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="dashboard/sign-up.html", context=context)


#SECTION :      login
def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    
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