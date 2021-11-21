from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('tenant/', views.tenantView, name="tenant"),
    path('eng/', views.engView, name="eng"),
    # using name makes the link dynamic
    path('login/', views.loginView, name="login"),
    path('qualification/', views.qualificationView, name="qualification"),
    path('aboutus/', views.aboutusView, name="aboutus"),
    path('contact/', views.contactView, name="contact"),
    path('tenant_form/', views.tenantApplicationView, name="tenantform"),
]
