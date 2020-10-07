from django import forms
from django.contrib.auth import get_user_model
from .models import Editor, Comment
User = get_user_model()

class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title'}))

    class Meta:
        model = Editor
        fields = ['title', 'category_selected','article_data','project_link',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_desc']

