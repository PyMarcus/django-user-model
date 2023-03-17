from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreateForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('first_name',
                    'last_name',
                    'email',
                    'phone',
                    'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name',
                                     'last_name',
                                     'phone')}),
        ('Permissions', {'fields': ('is_active',
                                    'is_staff',
                                    'is_superuser',
                                    'groups',
                                    'user_permissions')}),
        ('Important dates', {'fields': ('last_login',
                                       'date_joined')})
    )
