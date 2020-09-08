from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email_address'), unique=True)
    phone = models.CharField(_('phone_number'), max_length=20,unique=True)
    username = models.CharField(_('username'), max_length=100, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    objects = CustomUserManager()

class UserProfile(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    about_myself = models.TextField()
    date_of_birth = models.DateTimeField()
    hometown = models.CharField(max_length=254)
    present_location = models.CharField(max_length=254)
    geo_location = models.CharField(max_length=254)
    facebook = models.URLField(max_length=254, blank=True)
    website = models.URLField(max_length=254, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    interests = models.TextField(blank=True)

class Board(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    number_of_threads = models.IntegerField()
    number_of_posts = models.IntegerField()
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)

class Thread(models.Model):
    date_of_last_reply = models.DateTimeField()
    name_of_last_poster = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

class Post(models.Model):
    name_of_publisher = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    date_of_post = models.DateTimeField()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
