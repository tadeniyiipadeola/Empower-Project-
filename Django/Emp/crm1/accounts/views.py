from django.contrib.auth.models import Group, User
from django.http import request
from django.shortcuts import render, redirect
from .models import *
from .forms import *
import logging
from .backends import *
from .decorators import *
import pymongo

from django.contrib.auth.decorators import login_required
from django.contrib.auth import backends, login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from django.views.generic import ListView

from django_tables2 import SingleTableView
from .tables import *

from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)


def home(request):  
    user = request.user
    if user.is_authenticated:
        user_groups = user.groups.all()
        # print(user.groups.filter(name='ENG').exists())
        if user.groups.filter(name='ENG').exists():
            return redirect('eng')
        elif user.groups.filter(name='Tenant').exists():
            return redirect('tenant')
        elif user.groups.filter(name='Landlord').exists():
            return redirect('logout')
    return redirect('userloginpage')

# def upload_file_view(request):
#     form = PDF_ModelForm(request.POST or None, request.FILES or None)
#     if form.is_valid ():
#         model_instance = form.save(commit=False)
#         model_instance.save()
#         return HttpResponse("File uploaded successfully")

#     return render(request, 'accounts/upload.html', {'form': form})

def b_login(request):
    return render(request, 'accounts/bootstrap_login.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def app_tenants(request):
    return render(request, 'accounts/app_tenant.html')

def sidebar_real(request):
    return render(request, 'accounts/sidebar_real.html')

def inform_forms(request):
    return render(request, 'accounts/user/inform_forms.html')

def footer_boot(request):
    return render(request, 'accounts/footer_boot.html')

# def register(request):
#     if request.method == "POST":
#         form = registrationForm(request.POST)
#         if form.is_valid():
#             Type = request.POST['Type']
#             username = request.POST['username']
#             user = form.save()
#             group, created = Group.objects.get_or_create(name=Type)
#             group.user_set.add(user)
#             messages.success(request, "Registration successful.")
#             if Type == "Tenant":
#                 return redirect('tenantAccount')
#             return redirect('home')
#         messages.error(
#             request, "Unsuccessful registration. Invalid information.")
#     form = registrationForm()
#     return render(request, 'accounts/register.html', {'form': form})


# @unauthenticated_user
# def loginView(request):
#     context = {}

#     user = request.user
#     if user.is_authenticated:
#         return redirect('home')

#     if request.method == 'POST':
#         form = AccountAuthenticationForm(request.POST)
#         if form.is_valid():
#             print("Form is valid")
#             username = request.POST['username']
#             password = request.POST['password']
#             Type = request.POST['Type']
#             user = authenticate(username=username,
#                                 password=password, Type=Type)
#             print("Printing user: ", user)
#             if user is not None:
#                 login(request, user)
#                 print("User exists!")
#                 messages.info(
#                     request, f"You are now logged in as {user.first_name}.")
#                 logger.error('Something went right!')
#                 return redirect('home')
#             else:
#                 print("User does not exists!")
#                 messages.error(request, "Invalid username or password.")
#                 logger.error('Something went wrong!')
#         else:
#             print("Form is Invalid")
#             messages.error(request, "Invalid username or password.")
#             logger.error('Something went wrong!')
#     form = AccountAuthenticationForm()
#     context['login_form'] = form
#     return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    storage = messages.get_messages(request)
    for msg in storage:
        del msg
    messages.info(
        request, f"You are now logged out")
    return redirect('home')

def qualificationView(request):
    return render(request, 'accounts/qualification.html')

def aboutusView(request):
    return render(request, 'accounts/aboutus.html')


# def tenantApplicationView(request):
#     if request.method == 'POST':
#         fs = UploadFileForm(request.POST, request.FILES)
#         if fs.is_valid():
#         # uploaded_file = request.FILES['document']
#             form_instance = fs.save(commit=False)
#             form_instance.user = request.user
#             form_instance.save()

#             gridfs = GridFSStorage()
#             uploads = GridFSStorage(location='/uploads')

#             return redirect('home')
#     fs = UploadFileForm()

#     user_apps = None
#     queryset = Application.objects.all()
#     if queryset.exists():
#         user_apps = Application.objects.get(user = request.user)
#         print(user_apps.pdf)    
#     pdf_path = ""
#     if user_apps is not None:
#         pdf_path = user_apps.pdf
#     return render(request, 'accounts/application_tenant.html', {'form': fs, 'pdf_path': pdf_path})


# def contactView(request):
#     return render(request, 'accounts/contact.html')

# @allowed_users(allowed_roles=['Tenant'])
# def tenantAccount(request):
#     if request.method == 'POST':
#         form = tenantInfoForm(request.POST)
#         if form.is_valid():
#             form_instance = form.save(commit=False)
#             form_instance.user = request.user
#             form_instance.save()

            
#             client = pymongo.MongoClient("mongodb+srv://shubha:engdbmongo@firstcluster.sabqf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#             db = client.ENG_DB
#             print("db.Applications")
#             print(db.Applications.find_one())

#             return redirect('tenant')
#     form = tenantInfoForm()
#     info_obj = []
#     if tenantInformation.objects.all().exists():
#         info_obj = tenantInformation.objects.get(user= request.user)
#     # print(info_obj.address1)
#     return render(request, 'accounts/tenant_info.html', {'form': form, 'info_obj': info_obj})


# @allowed_users(allowed_roles=['Tenant'])
# def tenantView(request):
#     return render(request, 'accounts/tenant_dash.html')


# @allowed_users(allowed_roles=['ENG'])
# def engView(request):
#     return render(request, 'accounts/eng_dash.html')


# def allTenants(request):
#     queryset = tenantInformation.objects.all()
#     # print(queryset[0].address1)
#     table = TenantTable(queryset)
#     return render(request, 'accounts/all_tenants.html', {"objects": queryset, "table": table})

# def tenantEditView(request, username):
#     # print(user)
#     user = Account.objects.get(username=username)
#     if request.method == 'POST':
#         form = tenantInfoForm(request.POST)
#         if form.is_valid():
#             form_instance = form.save(commit=False)
#             form_instance.user = user
#             form_instance.save()
#             return redirect('editTenant', username=username)
#     form = tenantInfoForm()
#     info_obj = tenantInformation.objects.get(user= user)
#     return render(request, 'accounts/edit_tenant.html', {'form': form, 'user': user, 'info_obj': info_obj})
#     # return render(request, 'accounts/eng.html')

def homepage(request):
    return render(request, 'accounts/Homepage.html')

# ______________________________________________________________________________
#Temi working on this
#user sign up
def user_sign_up(request):
    if request.method =="POST":
        user_name = request.POST['username']
        
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.warning(request,"Password didn't matched")
            return redirect('userloginpage')
        
        try:
            if backends.UserModel.objects.all().get(username=user_name):
                messages.warning(request,"Username Not Available")
                return redirect('userloginpage')
        except:
            pass
            

        new_user = backends.UserModel.objects.create_user(username=user_name,password=password1)
        new_user.is_superuser=False
        new_user.is_staff=False
        new_user.save()
        messages.success(request,"Registration Successfull")
        return redirect("userloginpage")
    return HttpResponse('Access Denied')



#staff sign up
def staff_sign_up(request):
    if request.method =="POST":
        user_name = request.POST['username']
        
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.success(request,"Password didn't Matched")
            return redirect('staffloginpage')
        try:
            if User.objects.all().get(username=user_name):
                messages.warning(request,"Username Already Exist")
                return redirect("staffloginpage")
        except:
            pass
        
        new_user = User.objects.create_user(username=user_name,password=password1)
        new_user.is_superuser=False
        new_user.is_staff=True
        new_user.save()
        messages.success(request," Staff Registration Successfull")
        return redirect("staffloginpage")
    else:

        return HttpResponse('Access Denied')




#user login and signup page
def user_log_sign_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pswd']

        user = authenticate(username=email,password=password)
        try:
            if user.is_staff:
                
                messages.error(request,"Incorrect username or Password")
                return redirect('staffloginpage')
        except:
            pass
        
        if user is not None:
            login(request,user)
            messages.success(request,"successful logged in")
            print("Login successfull")
            return redirect('homepage')
        else:
            messages.warning(request,"Incorrect username or password")
            return redirect('userloginpage')

    response = render(request,'accounts/user/userlogsign.html')
    return HttpResponse(response)

    #staff login and signup page
def staff_log_sign_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        
        if user.is_staff:
            login(request,user)
            return redirect('staffpanel')
        
        else:
            messages.success(request,"Incorrect username or password")
            return redirect('staffloginpage')
    response = render(request,'accounts/staff/stafflogsign.html')
    return HttpResponse(response)



#logout for admin and user 
def logoutuser(request):
    if request.method =='GET':
        logout(request)
        messages.success(request,"Logged out successfully")
        print("Logged out successfully")
        return redirect('user')
    else:
        print("logout unsuccessfull")
        return redirect('userloginpage')


@login_required(login_url='/staff')
def staff_View_cust_Data(request):

    applied = UserLegal_info.objects.all()
    if not applied:
        messages.warning(request,"No Tenant application  Found")
    return HttpResponse(render(request,'accounts/staff/customer_table.html',{'applied':applied}))

