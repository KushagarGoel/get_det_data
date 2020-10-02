from django.db import models
from django.contrib.auth import get_user_model
from category.models import Category
# Create your models here.

User = get_user_model()
# Create your models here.
class Dataset(models.Model):
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    category_selected = models.ManyToManyField(Category)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title


class Contributor(models.Model):
    def get_upload_path(self,filename):
        return '{0}/{1}'.format(self.dataset_name.title, filename)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    dataset_name = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.dataset_name.title



