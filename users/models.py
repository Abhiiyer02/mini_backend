from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# class UserManager(BaseUserManager):
#     def create_superuser(self, email, username, first_name, password, **other_fields):
#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_active', True)
#         other_fields.setdefault('is_superuser', True)

#         if other_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must be assigned to is_staff=True.')
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_superuser=True.')

#         return self.create_user(email, username, first_name, password, **other_fields)

#     def create_user(self, email, username, first_name, password, **other_fields):
#         if not email:
#             raise ValueError(_('You must provie an email address'))

#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username,
#                           first_name=first_name, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user
#rama I'm back
#rama


# class User(AbstractUser, PermissionsMixin):

#     username = models.CharField(max_length=50, blank=True, null=True, unique=True)
#     email = models.EmailField(_('email address'), unique=True)
#     first_name = models.CharField(max_length=150, null=True, blank=True)
#     last_name = models.CharField(max_length=150, null=True, blank=True)
#     phone_no = PhoneNumberField(unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return "{}".format(self.email)

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, User_ID, username, email, password, is_staff, is_superuser, **extra_fields):
        # Creates and saves a User with the given username, email and password.
        now = timezone.now()
        if not User_ID:
            raise ValueError('The given User_ID must be set')
        email = self.normalize_email(email)
        user = self.model(User_ID=User_ID, username=username, email=email,     is_staff=is_staff, is_active=True, is_superuser=is_superuser, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, User_ID, username, email, password=None, **extra_fields):
        return self._create_user(User_ID, username, email, password, False, False,**extra_fields)

    def create_superuser(self, User_ID, username, email, password, **extra_fields):
        return self._create_user(User_ID, username, email, password, True, True,**extra_fields)

class CustomUser(AbstractUser):
    BRANCH_CHOICES = [
        ("CSE","Coputer Science and Engineering"),
        ("ISE","Information Science Engineering"),
        ("ECE","Electronics and Communication Engineering"),
        ("CV","Civil Engineering"),
        ("ME","Mechanical Engineering"),
        ("EEE","Elcectrical and Electronics Engineering"),
        ("EI","Electronics and Instrumentation Engineering"),
        ("IP","Industrial Production"),
        ("CSBS","Computer Science and Business Systems Engineering"),
        ("CTM","Construction Technology Management"),
        ("PST","Polymer Sceince Engineering"),
        ("BT","BioTechnology Engineering"),
        ("EV","Environmental Engineering"),
        # ("","Engineering"),
    ]    
    User_ID = models.CharField(max_length=15, primary_key=True, unique=True)
    branch = models.CharField(max_length=15, choices=BRANCH_CHOICES, default='Administration')

    objects = CustomUserManager()

    USERNAME_FIELD = 'User_ID'
    REQUIRED_FIELDS = ['email', 'username']