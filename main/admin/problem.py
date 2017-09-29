from django.contrib import admin

from main.models import Problem, TestData


class TestDataInline(admin.TabularInline):
    model = TestData
    fields = ('order', 'input_file', 'output_file', 'create_time',)
    readonly_fields = ('create_time',)


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'time_limit', 'memory_limit',
                    'released', 'deadline', 'contributor',
                    'testdata_num', 'accept_rate', 'is_deleted',)
    list_display_links = ('number', 'title',)
    list_editable = ('released', 'contributor', 'is_deleted',)
    fields = ('number', 'title', 'time_limit', 'memory_limit',
              'desc', 'input_desc', 'output_desc',
              'input_sample', 'output_sample', 'hint',
              'deadline', 'released', 'is_deleted', 'contributor',
              'create_time', 'submit_cnt', 'accept_cnt', 'compare_file',)
    readonly_fields = ('create_time', 'submit_cnt', 'accept_cnt',)
    inlines = [TestDataInline,]
