from django.contrib import admin
from .models import *


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ("task", "start_data", "end_data", "priority")
    search_fields = ("task", "start_data")
    list_filter = ("start_data", "end_data", "priority")


admin.site.register(ToDoList, ToDoListAdmin)
