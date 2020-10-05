from django import forms
from django.contrib.auth import get_user_model
from .models import Dataset
User = get_user_model()




class CreateDataset(forms.ModelForm):

    class Meta:
        model = Dataset
        fields = ['title','category_selected','description','dataset_type']


