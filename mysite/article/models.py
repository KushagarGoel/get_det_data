from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Editor(models.Model):
    arti = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.arti