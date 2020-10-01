from django.contrib import admin
from .models import Editor, Comment
# Register your models here.

class EditorAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    list_display = ['title', 'active','updated']
    readonly_fields = ['updated', 'timestamp']


    class Meta:
        model = Editor

admin.site.register(Editor, EditorAdmin)
admin.site.register(Comment)