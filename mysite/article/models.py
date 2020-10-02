from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from category.models import Category
# Create your models here.

User = get_user_model()

class Editor(models.Model):
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    article_data = RichTextField(null=True, blank=True)
    category_selected = models.ManyToManyField(Category)
    project_link = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)



    def __str__(self):
        return self.title

class Comment(models.Model):
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    comment_desc = models.TextField(null=False, blank=False)
    article_id = models.ForeignKey(Editor, on_delete=models.CASCADE)