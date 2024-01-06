from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group

from dashboard.forms import SignUpForm, EditProfileForm
from blog.models import Blog



#SECTION :      dashboard

#NOTE :         dashboard
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login_view")
    
    context = {
        "user": request.user
    }
    
    # print(request.user.groups.all())
    
    return render(request=request, template_name="dashboard/dashboard.html", context=context)


#NOTE :         edit profile
def edit_profile_view(request):
    if not request.user.is_authenticated:
        return redirect("login_view")
    
    
    form = EditProfileForm(instance=request.user)
    
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            
            return redirect("dashboard")
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="dashboard/edit-profile.html", context=context)


#NOTE :         change password
def change_password_view(request):
    if not request.user.is_authenticated:
        return redirect("login_view")

    
    form = PasswordChangeForm(user=request.user)
    
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        
        if form.is_valid():
            form.save()
            
            logout(request=request)
            
            return redirect("login_view")
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="dashboard/change-password.html", context=context)


#NOTE :         blogs
def blogs_view(request):
    if not request.user.is_authenticated:
        return redirect("login_view")
    
    
    blogs = Blog.objects.all()
    
    context = {
        "blogs": blogs
    }
    
    return render(request=request, template_name="dashboard/blogs.html", context=context)



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
            
            group = Group.objects.get(name="Editor")
            user.groups.add(group)
            
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