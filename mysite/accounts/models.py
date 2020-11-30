from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from category.models import Category
from django.conf import settings
import random
import hashlib
from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.db.models.signals import post_save
# Create your models here.

User = get_user_model()

RATING_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
)

class UserDetails(models.Model):
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    interested_category = models.ManyToManyField(Category)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES, default=3)
    github_link = models.CharField(max_length=200, null=True, blank=True)
    linkedin_link = models.CharField(max_length=200, null=True, blank=True)
    active_user = models.BooleanField(default=True)
    worked = models.BooleanField(default=False)
    provided_job = models.BooleanField(default=False)
    provided_payment = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.username.username




class EmailConfirmed(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=200)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.confirmed)

    def activate_user_email(self):
        activation_url = '%s%s'%(settings.SITE_URL,reverse("activation_view", args=[self.activation_key]))
        context = {
            'activation_key': self.activation_key,
            'activation_url': activation_url,
        }
        message = render_to_string("accounts/activation_message.txt", context)
        subject = "Activate your account"
        print(message)
        self.email_user(subject, message,settings.DEFAULT_FROM_EMAIL)

    def email_user(self, subject, message, from_email=None, **kwargs):
        yo = send_mail(subject, message,from_email,[self.user.email], **kwargs)





def user_created(sender, instance, created, *args, **kwargs):
    if created:
        email_confirmed, email_is_created = EmailConfirmed.objects.get_or_create(user= instance)
        if email_is_created:
            short_hash = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
            username = instance.username
            activation_key = hashlib.sha1(str(username+short_hash).encode('utf-8')).hexdigest()
            email_confirmed.activation_key = activation_key
            email_confirmed.save()
            email_confirmed.activate_user_email()



post_save.connect(user_created, sender=User)


