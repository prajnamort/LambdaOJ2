from django.contrib import admin

from main.models import Problem


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'time_limit', 'memory_limit',
                    'desc', 'sample_num', 'deadline', 'released', 'contributor',)
    list_display_links = ('number', 'title')
    fields = ('number', 'title', 'time_limit', 'memory_limit',
              'desc', 'input_desc', 'output_desc',
              'input_sample', 'output_sample', 'hint',
              'sample_num', 'deadline', 'released', 'contributor',
              'create_time',)
    readonly_fields = ('create_time',)
