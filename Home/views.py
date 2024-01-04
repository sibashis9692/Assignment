from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


class profile(View):
    def get(self, request):
        return render(request, "profile.html")
    

class login_view(View):
    def post(self, request):

        fm = LoginForm(request.POST)

        if(fm.is_valid()):

            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
        
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('/')
            
            messages.error(request, "Invalid credentials")
        return redirect('/login/')
        
    def get(self, request):

        form = LoginForm()

        context = {
            "form" : form
        }

        return render(request, "login.html", context)
    
class registration(View):

    def get(self, request):
        form = RegistrationForm()

        context = {
            "form" : form
        }

        return render(request, "register.html", context)
    
    def post(self, request):

        form = RegistrationForm(request.POST)

        if(form.is_valid()):

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            Confirm_Password = form.cleaned_data['password_confirmation']

            exist_username = User.objects.filter(username = username).first()
            exist_email = User.objects.filter(email = email).first()

            if(not exist_username):
                if(not exist_email):
                    if(password == Confirm_Password):
                        
                        user = User.objects.create(username = username, email = email)
                        user.set_password(password)
                        user.save()

                        messages.success(request, "User Create sucessfully")

                        return redirect("/login/")
                    
                    messages.error(request, "Password and Conform Password is not same")
                    return redirect("/register/")   
                messages.error(request, "Given Email is Alrady exists")
                return redirect("/register/")   
            messages.error(request, "Username is Alrady taken")
        return redirect("/register/")   
    
@login_required(login_url='/login/')
def profile_page(request):
    user = request.user

    data = User.objects.filter(username = user.username).first()

    context = {
        "data" : data
    }

    return render(request, "profile.html", context)

@login_required(login_url='/login/')
def logout_page(request):

    logout(request)

    return redirect("/login/")