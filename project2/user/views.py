from django.shortcuts import render
from .forms import registerForm,loginForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import View


class registerUser(View):
    def get(self, request):
        rF = registerForm
        return render(request, 'register.html',{'rF':rF})
    
    def post(self, request):
        rF = registerForm(request.POST)
        if rF.is_valid():
            username = rF.cleaned_data.get('username')
            email = rF.cleaned_data.get('email')
            password = rF.cleaned_data.get('password')
            password_confirmation = rF.cleaned_data.get('password_confirmation')
            if password == password_confirmation:
                user = User(username=username, email=email, password=make_password(password))
                user.save()
                return redirect(reverse_lazy('User:login'))
            else:
                rF.add_error('password_confirmation', "Passwords don't match.")
        return render(request, 'register.html', {'rF': rF})
    
    
class loginUser(View):
    def get(self, request):
        lF = loginForm()
        return render(request, 'login.html', {'lF': lF})

    def post(self, request):
        lF = loginForm(request.POST)
        if lF.is_valid():
            username = lF.cleaned_data['username']
            password = lF.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('book:book_list'))
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid input.')
        return redirect('User:login')

def logoutUser(request):
    logout(request)
    return redirect('book:book_list')