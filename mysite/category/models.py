from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    active_fields = models.BooleanField(default=True)

class RequesteCategory(models.Model):
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    requested_cat = models.CharField(max_length=100)
    category_desc = models.TextField(blank=True, null=True)