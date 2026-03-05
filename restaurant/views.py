from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
UserCreationForm
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def book(request):
    return render(request, 'book.html')
def menu(request):
    return render(request, 'menu.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
            form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})