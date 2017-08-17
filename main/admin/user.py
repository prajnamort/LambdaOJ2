from django.contrib.auth.admin import UserAdmin as OrigUserAdmin
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from main.models import User


@admin.register(User)
class UserAdmin(OrigUserAdmin):
    fieldsets = (
        (None,
         {'fields': ('username', 'email', 'mobile', 'student_id', 'password')}),
        (_('Personal info'),
         {'fields': ('first_name', 'last_name')}),
        (_('Permissions'),
         {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'),
         {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('last_login', 'date_joined',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'mobile', 'student_id', 'password1', 'password2'),
        }),
    )
    list_display = ('id', 'username', 'email', 'mobile', 'student_id', 'is_staff')
    list_display_links = ('id', 'username')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email', 'mobile', 'student_id')
    ordering = ('id',)
