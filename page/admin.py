from django.contrib import admin
from .models import Project,Task 
# Register your models here.

class TaskInline(admin.TabularInline):
    model = Task 

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ 
        TaskInline
    ]
admin.site.register(Task)