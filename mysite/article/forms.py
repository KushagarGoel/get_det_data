from django import forms
from django.contrib.auth import get_user_model
from .models import Editor, Comment
User = get_user_model()

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Editor
        fields = ['title','article_data', 'category_selected','project_link',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_desc']

