from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import logging
from .backends import *
from .decorators import *


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib import messages
# Create your views here.

logger = logging.getLogger(__name__)

# ____________________________________________________________________________


def home(request):
    user = request.user
    if user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def register(request):
    if request.method == "POST":
        form = tenantRegistrationForm(request.POST)
        if form.is_valid():
            Type = form.cleaned_data['Type']
            print(Type)
            group = Group.objects.get(name=Type)
            user = form.save()
            user.groups.add(group)
            login(request, user, backend='CaseInsensitiveModelBackend')
            messages.success(request, "Registration successful.")
            return redirect("dashboard")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = tenantRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


@unauthenticated_user
def loginView(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            Type = request.POST['Type']
            user = authenticate(email=email, password=password, Type=Type)

            if user is not None:
                login(request, user)
                messages.info(
                    request, f"You are now logged in as {user.first_name}.")
                logger.error('Something went right!')
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password.")
                logger.error('Something went wrong!')
        else:
            messages.error(request, "Invalid username or password.")
            logger.error('Something went wrong!')
    form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('home')


def qualificationView(request):
    return render(request, 'accounts/qualification.html')


def aboutusView(request):
    return render(request, 'accounts/aboutus .html')

def tenantApplicationView(request):
    return render(request, 'accounts/Application_tenant.htm')

def contactView(request):
    return render(request, 'accounts/contact.html')


@allowed_users(allowed_roles=['Tenant'])
def tenantView(request):
    return render(request, 'accounts/tenant.html')


@allowed_users(allowed_roles=['ENG'])
def engView(request):
    return render(request, 'accounts/eng.html')
