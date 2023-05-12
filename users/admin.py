from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'User_ID',
        'username',
        'email',
        'first_name',
        'last_name',
        'branch',
        'is_staff',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields':('User_ID', 'branch',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields':('User_ID', 'branch',)}),)

admin.site.register(CustomUser, CustomUserAdmin)    
