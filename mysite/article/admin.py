from django.contrib import admin
from .models import Editor, Comment
# Register your models here.

class EditorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Editor

admin.site.register(Editor, EditorAdmin)
admin.site.register(Comment)