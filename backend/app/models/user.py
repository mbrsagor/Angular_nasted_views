import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from app.utils.type import UserRole, Gender
from app.manager import UserManager

class Union(models.Model):
    name = models.CharField(max_length=150)
    world_no = models.IntegerField(default=1)

    class Meta:
        unique_together = ('name', 'world_no',)
    
    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, unique=True)
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14, unique=True)
    is_candidate = models.BooleanField(default=False)
    role = models.IntegerField(choices=UserRole.select_role(), default=UserRole.CITIZEN.value)
    gender = models.IntegerField(choices=Gender.select_gender(), default=Gender.MALE.value)
    education = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=200)
    union_name = models.ForeignKey(Union, on_delete=models.CASCADE, related_name='user_union', null=True)
    brand = models.ImageField(upload_to='brand', blank=True, null=True)
    nid = models.CharField(max_length=200)
    age = models.IntegerField(default=18)
    date_of_birth = models.DateField(default=datetime.date.today)
    profile_picture = models.ImageField(upload_to='user', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    def __str__(self):
        if self.email:
            return self.email
        else:
            return self.phone_number
