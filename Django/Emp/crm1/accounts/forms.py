# forms.py
# from typing import Optional
# from django.forms import ModelForm
# from django import forms
# from .models import *
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate


# class registrationForm(UserCreationForm):
#     class Meta:
#         model = Account
#         fields = ['first_name', 'last_name', "email", "username", 'Type']

# class PDF_ModelForm(forms.ModelForm):
#    class Meta:
#       model = PDF
#       fields = ('file_name',)


# class AccountAuthenticationForm(forms.ModelForm):
#     password = forms.CharField(label="Password", widget=forms.PasswordInput)

#     class Meta:
#         model = Account
#         fields = ('username', 'password', 'Type')

#     def clean(self):
#         if self.is_valid():
#             username = self.cleaned_data['username']
#             password = self.cleaned_data['password']
#             Type = self.cleaned_data['Type']
            # if not authenticate(username=username, password=password, Type=Type):
            #     raise forms.ValidationError("Invalid login")


# class tenantInfoForm(ModelForm):
#     class Meta:
#         model = tenantInformation
#         fields = ['address1', 'address2', 'city', 'zip_code', 'county']

# class UploadFileForm(ModelForm):
#     class Meta:
#         model = Application
#         fields = ['pdf']
