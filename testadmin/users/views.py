from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
# Create your views here.

def users(request):
    # if request.method == "POST":
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
    # else:
    #     form = RegisterForm()
    return render(request, 'main/index.html')     


