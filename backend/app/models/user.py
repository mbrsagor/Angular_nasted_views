from django.contrib.auth.models import AbstractUser
from django.db import models

from app.utils.type import UserRole, Gender
from app.manager import UserManager

class User(AbstractUser):
    email = models.EmailField(blank=True, unique=False)
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14, unique=True)
    is_candidate = models.BooleanField(default=False)
    role = models.IntegerField(choices=UserRole.select_role(), default=UserRole.CITIZEN.value)
    gender = models.IntegerField(choices=Gender.select_gender(), default=Gender.MALE.value)
    address = models.CharField(max_length=200)
    world_no = models.IntegerField(default=1)
    brand = models.ImageField(upload_to='brand', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='user', blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number
