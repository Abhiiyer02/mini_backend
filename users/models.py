from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class UserManager(BaseUserManager):
    def create_superuser(self, email, username, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, first_name, password, **other_fields)

    def create_user(self, email, username, first_name, password, **other_fields):
        if not email:
            raise ValueError(_('You must provie an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser, PermissionsMixin):

    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone_no = PhoneNumberField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return "{}".format(self.email)

class Student(User):
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
    USN = models.CharField(max_length=15, primary_key=True)
    branch = models.CharField(max_length=4, choices=BRANCH_CHOICES)
    # Create a TextChoice List of Branches

    USERNAME_FIELD = 'USN'
    REQUIRED_FIELDS = ['email', 'first_name', 'phone_no', 'branch', 'username']
 