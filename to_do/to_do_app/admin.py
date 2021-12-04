from django.contrib import admin
from .models import *

class PostForm(forms.ModelForm):
    def clean(self):
        start_data = self.cleaned_data['start_data']
        end_data = self.cleaned_data['end_data']
        if start_data > end_data:
            raise forms.ValidationError({'start_data': "Cant be more end date!"})

class ToDoListAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('task', 'start_data', 'end_data', 'priority')
    search_fields = ('task', 'start_data')
    list_filter = ('start_data', 'end_data', 'priority')


admin.site.register(ToDoList, ToDoListAdmin)

