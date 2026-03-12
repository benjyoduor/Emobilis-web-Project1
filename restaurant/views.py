from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django_daraja.mpesa.core import MpesaClient
from restaurant.models import Meal
UserCreationForm
from django.contrib.auth import login
from restaurant.models import  Payment
from django.contrib.auth import authenticate

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def book(request):
    return render(request, 'book.html')
def menu(request):
    return render(request, 'menu.html')
def signup(request):
    return render(request, 'signup.html')


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


def home(request):
    meals = Meal.objects.filter(available=True)
    return render(request, 'index.html', {'meals': meals})


def pay(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        amount = request.POST.get("amount")

        if not phone or not amount:
            messages.error(request, "All fields are required.")
            return render("menu.html")

        try:
            client = MpesaClient()

            response = client.stk_push(
                phone,
                int(amount),
                "EMOBILIS",
                f"Payment for {phone}",
                "https://example.com/callback/"
            ).json()

            Payment.objects.create(
                user=request.user,
                phone=phone,
                amount=amount,
                checkout_request_id=response.get("CheckoutRequestID", ""),
                status="Pending"
            )

            messages.success(request, "STK push sent! Check your phone.")

        except Exception:
            messages.error(request, "Payment failed.")
    return render(request, 'menu.html')