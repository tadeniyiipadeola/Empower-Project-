from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

from . models import *



# class AccountAdmin(UserAdmin):
#     list_display = ('fname', 'lname' , 'address1', 'zipcode', 'gender', 'email','phone')
#     search_fields = ('fname', 'lname')


#     # filter_horizontal = ()
#     # list_filter = ()
#     # fieldsets = ()
admin.site.register(UserLegal_info)
# admin.site.register(Account, AccountAdmin)
# admin.site.register(tenantInformation)
# admin.site.register(Application)