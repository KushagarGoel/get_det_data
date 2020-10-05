from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from category.models import Category
from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.db.models.signals import post_save
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
    description = models.TextField( default = "yo")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/datasets/%s'%(self.title)


class Contributor(models.Model):
    def get_upload_path(self,filename):
        return 'datasets/{0}/{1}'.format(self.dataset_name.title, filename)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    dataset_name = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.dataset_name.title



class ContributrFolder(models.Model):
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    file_count = models.CharField(max_length = 200)

    def __str__(self):
        return str(self.username)

class PremiumDataset(models.Model):
    def get_upload_path(self, filename):
        return 'datasets_premium/{0}/{1}'.format(self.dataset_name, filename)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    dataset_name = models.CharField(max_length = 100, unique = True)
    file = models.FileField(upload_to = get_upload_path, null = True)
    sale_price = models.DecimalField(max_digits=20, decimal_places=2)
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.username)

    def create_dataset(self):
        message = "Dataset has been recieved for review"
        subject = "Review Dataset"
        print(message)
        self.email_me(subject, message,settings.DEFAULT_FROM_EMAIL)

    def activate_dataset(self):
        message = "Your Dataset is active now"
        subject = "Review Dataset"

        self.email_user(subject, message,settings.DEFAULT_FROM_EMAIL)

    def email_me(self, subject, message, from_email=None, **kwargs):
        yo = send_mail(subject, message,from_email,['kushagargoel28@gmail.com'], **kwargs)

    def email_user(self, subject, message, from_email=None, **kwargs):
        yo = send_mail(subject, message,from_email,[self.username.email], **kwargs)




def dataset_created(sender, instance, created, *args, **kwargs):
    print(type(instance))
    if created:
        instance.create_dataset()
    else:
        if instance.active == True:
            instance.activate_dataset()



post_save.connect(dataset_created, sender=PremiumDataset)

