from django.db import models

class Users(models.Model):
    ROLE_CHOICES = [(0, 'Admin'), (1, 'Moderator'), (2, 'Member')]
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=254)
    username = models.CharField(max_length=254, blank=True)
    user_role = models.CharField(max_length=10, choices=ROLE_CHOICES)

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
    name_of_last_poster = models.ForeignKey('Users', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

class Post(models.Model):
    name_of_publisher = models.ForeignKey('Users', on_delete=models.CASCADE)
    date_of_post = models.DateTimeField()
