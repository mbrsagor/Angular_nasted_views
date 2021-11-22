from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    email = models.EmailField(blank=True, unique=False)
    phone_number = models.CharField(max_length=14, unique=True)
    nid_number = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=500, blank=True)
    union = models.CharField(max_length=100, blank=True)
    word_number = models.IntegerField(default=1, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    MALE = 1
    FEMALE = 2
    OTHERS = 3
    CHOICES_GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    )
    gender = models.PositiveSmallIntegerField(choices=CHOICES_GENDER, null=True, blank=True)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_picture', blank=True, null=True)
    cover_photo = models.ImageField(default='default.jpg', upload_to='cover_photo', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    @property
    def make_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"
