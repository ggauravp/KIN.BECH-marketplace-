from django.shortcuts import render, redirect
from django.contrib.auth import logout
from item.models import Category,Item
from .forms import SignupForm
from django.contrib import messages


def index(request):
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)[0:9][::-1]

    return render(request, 'core/index.html',{
        'categories':categories,
        'items': items,
    })

def  contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def log_out(request):
    logout(request)
    messages.success(request,"Your are logged out")
    return redirect('myapp:index')
