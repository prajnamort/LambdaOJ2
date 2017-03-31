from django.contrib import admin

from main.models import Problem


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'time_limit', 'memory_limit',)
    fields = ('order', 'title', 'time_limit', 'memory_limit', 'create_time',)
    readonly_fields = ('create_time',)
