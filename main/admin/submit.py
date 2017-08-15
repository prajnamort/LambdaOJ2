from django.contrib import admin

from main.models import Submit


@admin.register(Submit)
class SubmitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'problem', 'language', 'create_time',)
    fields = ('user', 'problem', 'language', 'code',
              'create_time',)
    readonly_fields = ('create_time',)
