from django.contrib import admin
from .models import LoanApplication, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)

admin.site.register(LoanApplication)