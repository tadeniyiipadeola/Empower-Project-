from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db.models import deletion
# from django.db.models.expressions import Value

# Create your models here.


# __________________________________________________________________________________________

# class MyAccountManager(BaseUserManager):
#     def create_user(self, first_name, last_name, email, username, Type, password=None):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not username:
#             raise ValueError("Users must have a username")
            
#         user = self.model(
#             first_name = first_name,
#             last_name = last_name,
#             email=self.normalize_email(email),
#             username=username,
#             Type=Type,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, first_name, last_name, email, username, password):
#         user = self.create_user(
#             first_name = first_name,
#             last_name = last_name,
#             email=self.normalize_email(email),
#             password=password,
#             username=username,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db) 
#         return user

# class PDF(models.Model):
#      file_name = models.FileField(upload_to='csvs')
#      uploaded = models.DateTimeField(auto_now_add=True)
#      activated = models.BooleanField(default=False)

#      def __str__(self):
#          return f"file id: {self.id}"

# class Account(AbstractBaseUser, PermissionsMixin):
#     first_name = models.CharField(verbose_name="first_name", default="John", max_length=30, unique=False)
#     last_name = models.CharField(verbose_name="lastname", default="Doe", max_length=30, unique=False)
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     CHOICES=[('Tenant','Tenant'),
#          ('ENG','ENG'),
#          ('Landlord', 'Landlord')]

#     Type = models.CharField(
#         max_length=60,
#         choices=CHOICES,
#         default='Tenant',
#     )

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'Type']

#     objects = MyAccountManager()

#     def __str__(self):
#         return self.email
    
#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, add_label):
#         return True
# -----------------------------------------------------------------------------

class UserLegal_info(models.Model):
    # CHOICES=[('Tenant','Tenant'),
    #      ('ENG','ENG'),
    #      ('Landlord', 'Landlord')]
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    fname = models.CharField(max_length= 15,),
    lname = models.CharField(max_length = 25,), 
    address1 = models.CharField(max_length=40,),
    address2 = models.CharField(max_length=40),
    city = models.CharField(max_length = 100, null=False),
    state = models.CharField(max_length=100, null=False),
    zipcode = models.IntegerField(max_length=5,null=False),
    drivers_license = models.IntegerField(max_length=12),
    phone = models.CharField(max_length=10, null=False),
    email = models.CharField(max_length=60, null=False),
    date_joined = models.DateTimeField(auto_now=True),
    tenant = models.ForeignKey(User, on_delete= models.CASCADE),



    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    HouseSize = models.IntegerField(max_length = 12),
    Income = models.IntegerField(max_length=10),
    MonthlyRent = models.IntegerField(max_length=10),

    Employeer = models.CharField(max_length=40)
    Job = models.CharField(max_length=50)
    birthDate = models.DateField()


   

# ------------------------------------------------------------------------
# class Customer(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     phone = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)

#     def __str__(self):
#         return self.name


# class Tag(models.Model):
#     name = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return self.name


# class Product(models.Model):
#     CATEGORY = (
#         ('Indoor', 'Indoor'),
#         ('Out Door', 'Out Door'))

#     name = models.CharField(max_length=200, null=True)
#     price = models.FloatField(max_length=200, null=True)
#     category = models.CharField(max_length=200, null=True, choices=CATEGORY)
#     description = models.CharField(max_length=200, null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     tags = models.ManyToManyField(Tag)

#     def __str__(self):
#         return self.name


# class Order(models.Model):
#     STATUS = (
#              ('Pending', 'Pending'),
#              ('Out for delivery', 'Out for delivery'),
#              ('Delivered', 'Delivered'))

#     customer = models.ForeignKey(
#         Customer, null=True, on_delete=models.SET_NULL)
#     products = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     status = models.CharField(max_length=200, null=True, choices=STATUS)

#     def __str__(self):
#         return self.products
