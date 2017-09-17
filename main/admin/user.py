from django.contrib.auth.admin import (
    UserAdmin as OrigUserAdmin, PermissionDenied,
    sensitive_post_parameters_m, unquote,)
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from main.models import User, MultiUserUpload


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
            'fields': ('username', 'email', 'mobile', 'student_id',
                       'password1', 'password2'),
        }),
    )
    list_display = ('id', 'username', 'email', 'mobile', 'student_id',
                    'groups_str', 'is_staff', 'is_superuser')
    list_display_links = ('id', 'username')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email', 'mobile', 'student_id')
    ordering = ('-is_superuser', '-is_staff')

    def groups_str(self, obj):
        return ','.join([g.name for g in obj.groups.all()])

    # 禁止普通 staff 修改（包括新增时） is_superuser 状态。
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:  # Superuser
            return self.readonly_fields
        return self.readonly_fields + ('is_superuser',)

    # 禁止普通 staff 查看和修改 Superuser 的资料。
    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        elif request.user.is_superuser:  # Superuser
            return True
        elif obj.is_superuser:  # obj is Superuser
            return False
        else:
            return True

    # 禁止普通 staff 修改 Superuser 的密码。
    @sensitive_post_parameters_m
    def user_change_password(self, request, id, form_url=''):
        user = self.get_object(request, unquote(id))
        if not self.has_change_permission(request, user):
            raise PermissionDenied
        return super().user_change_password(request, id, form_url)


@admin.register(MultiUserUpload)
class MultiUserUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_time',)
    fields = ('csv_content', 'results', 'create_time',)
    readonly_fields = ('results', 'create_time',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.fields
        return self.readonly_fields
