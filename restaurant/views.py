from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
UserCreationForm
from django.contrib.auth import login
from restaurant.models import Persons

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

def make_booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        person = (request.POST.get('person'))

        Persons.objects.create(
            name=name,
            email=email,
            phone=phone,
            person=person
        )
        return redirect('index')
    return render(request, 'booking.html')
