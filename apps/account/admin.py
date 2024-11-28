from django.contrib import admin

from apps.account.forms import CustomUserCreationForm
from apps.account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['id', 'username', 'email', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Permission', {'fields': ('is_active',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active',)
        }),
    )

    ordering = ('email',)