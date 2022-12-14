from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import NewUserForm
from .models import Account, Transaction


def homepage(request):
    if request.user.is_authenticated:
        account = get_object_or_404(Account, user=request.user)
    else:
        account = Account.objects.all()
    return render(request=request, template_name="tracker/home.html", context={'account': account})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            Account.objects.create(user=user)
            return redirect("tracker:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="tracker/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("tracker:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="tracker/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("tracker:homepage")


def debit_form(request):
    account = Account.objects.get(user=request.user)
    return render(request=request, template_name="tracker/debit.html", context={'account': account})


def debit(request):
    account = Account.objects.get(user=request.user)
    amount = float(request.POST['debit'])
    Transaction.objects.create(user=account, debit=amount)
    account.debit += amount
    account.balance += amount
    account.save()
    return HttpResponseRedirect(reverse('tracker:homepage'))


def credit_form(request):
    account = Account.objects.get(user=request.user)
    return render(request=request, template_name="tracker/credit.html", context={'account': account})


def credit(request):
    account = Account.objects.get(user=request.user)
    amount = float(request.POST['credit'])
    Transaction.objects.create(user=account, credit=amount)
    account.credit -= amount
    account.balance -= amount
    account.save()
    return HttpResponseRedirect(reverse('tracker:homepage'))
