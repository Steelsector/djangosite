from django.contrib import admin
from firstapp.models import Skill
from firstapp.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo']
    list_filter = ['technologies']
    search_fields = ['name']


admin.site.register(Skill)
admin.site.register(Project, ProjectAdmin)
