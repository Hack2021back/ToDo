from django.contrib import admin
from .models import *

<<<<<<< HEAD

class ToDoListAdmin(admin.ModelAdmin):
    list_display = ("task", "start_data", "end_data", "priority")
    search_fields = ("task", "start_data")
    list_filter = ("start_data", "end_data", "priority")

=======
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
>>>>>>> 39ddfe66ce2a96666510953add1717ce72b32f6a


admin.site.register(ToDoList, ToDoListAdmin)

