from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()


# Unregister the default User admin
admin.site.unregister(User)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Custom admin for User model.
    Extends Django's default UserAdmin with additional functionality.
    """
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)

