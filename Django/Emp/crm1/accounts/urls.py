from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('app_tenant/', views.app_tenants, name="app_tenant" ),
    path('sidebar_real/', views.sidebar_real, name="sidebar_real" ),
    # path('register/', views.register, name="register"),
    path('logout/', views.logout_view, name="logout"),
    # path('tenant/', views.tenantView, name="tenant"),
    # path('tenant_info/', views.tenantAccount, name="tenantAccount"),
    # path('eng/', views.engView, name="eng"),
    # path('login/', views.loginView, name="login"),
    path('b_login', views.b_login, name='b_login'),
    path('qualification/', views.qualificationView, name="qualification"),
    path('aboutus/', views.aboutusView, name="aboutus"),
    # path('contact/', views.contactView, name="contact"),
    # path('tenant_form/', views.tenantApplicationView, name="tenantform"),
    # path('manage_tenants/', views.allTenants, name="allTenants"),
    # path('edit_tenant/(?P<username>\w+)', views.tenantEditView, name="editTenant"),
    path('inform_forms/', views.inform_forms, name='inform_forms'),
    # path('upload/', upload_file_view, name='upload-view'),
    path('Homepage/', views.homepage, name="Homepage"),

    # ---------------------------------------------------------------------------

    path('user', views.user_log_sign_page,name="userloginpage"),
    path('user/login', views.user_log_sign_page,name="userloginpage"),

    path('user/signup', views.user_sign_up,name="usersignup"),

    path('staff/', views.staff_log_sign_page,name="staffloginpage"),
    path('staff/login', views.staff_log_sign_page,name="staffloginpage"),
    path('staff/signup', views.staff_sign_up,name="staffsignup"),

    path('logout', views.logoutuser,name="logout"),

#  this where the staff views the customer application tables 
    path('staff/customerData', views.staff_View_cust_Data, name ="staffpanel")
]
