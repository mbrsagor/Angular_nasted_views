from django.db import models
from app.models.user import Profile


class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Symbol(BaseEntity):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='symbol')

    def __str__(self):
        return self.name


class Nomination(BaseEntity):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='nominationProfile')
    qualification = models.CharField(max_length=300)
    profession = models.CharField(max_length=100)
    eduction = models.CharField(max_length=100)
    present_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    email_address = models.EmailField(max_length=200, blank=True, null=True)
    father_name = models.CharField(max_length=80)
    mother_name = models.CharField(max_length=80)
    is_approve = models.BooleanField(default=False)

    CHAIRMAN = 1
    MEMBER = 2
    WORDCHAIREMAN = 3
    CHOICES_POSITION = (
        (CHAIRMAN, 'Chairman'),
        (MEMBER, 'Member'),
        (WORDCHAIREMAN, 'Word Chairman'),
    )
    position = models.PositiveSmallIntegerField(choices=CHOICES_POSITION)
    symbol_name = models.ForeignKey(Symbol, on_delete=models.CASCADE, related_name='symbol')

    def __str__(self):
        return self.user_id
