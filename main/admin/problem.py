from django.contrib import admin

from main.models import Problem


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'time_limit', 'memory_limit',
                    'desc', 'input_desc', 'output_desc',
                    'input_sample', 'output_sample', 'hint',
                    'sample_num', 'deadline', 'released', 'contributor',)
    fields = ('order', 'title', 'time_limit', 'memory_limit',
              'desc', 'input_desc', 'output_desc',
              'input_sample', 'output_sample', 'hint',
              'sample_num', 'deadline', 'released', 'contributor',)
    readonly_fields = ('create_time',)
