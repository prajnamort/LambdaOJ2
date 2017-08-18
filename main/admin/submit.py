from django.contrib import admin

from main.models import Submit


@admin.register(Submit)
class SubmitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'problem', 'language', 'create_time',)
    fields = ('user', 'problem', 'language', 'code',
              'create_time',)
    readonly_fields = ('create_time',)

    # 禁止普通 staff 修改任何 Submit 内容（只能查看）。
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:  # Superuser
            return self.readonly_fields
        return self.fields
