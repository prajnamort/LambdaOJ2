from django.contrib import admin

from main.models import Submit


@admin.register(Submit)
class SubmitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'problem', 'language',
                    'judge_status', 'score', 'create_time', 'detail_link',)
    fields = ('user', 'problem', 'language', 'code',
              'judge_status', 'compile_status', 'run_results',
              'error_message', 'score', 'create_time',)
    readonly_fields = ('create_time',)
    search_fields = ('=id', '^user__username',)

    def detail_link(self, obj):
        return '<a href="/#/submit/{id}">查看提交详情</a>'.format(id=obj.id)
    detail_link.allow_tags = True

    # 禁止普通 staff 修改任何 Submit 内容（只能查看）。
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:  # Superuser
            return self.readonly_fields
        return self.fields
