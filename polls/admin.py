from django.contrib import admin
from .models import Poll, Question

# Register your models here.


class QuestionInline(admin.TabularInline):
    model = Question

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra


class PollAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['start_date']
        else:
            return []


admin.site.register(Poll, PollAdmin)
admin.site.register(Question)
