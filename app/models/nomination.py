from django.db import models
from app.models.user import Profile


class Symbol(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='symbol')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Nomination(models.Model):
    candidate = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='nominationProfile')
    certificate_name = models.CharField(max_length=90)
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
    status = models.BooleanField(default=False)
    position = models.PositiveSmallIntegerField(choices=CHOICES_POSITION)
    symbol_name = models.ForeignKey(Symbol, on_delete=models.CASCADE, related_name='symbol')
    created_at = models.DateTimeField(auto_now_add=True)

    def position_humanity(self):
        if self.position == 1:
            return "Chairman"
        elif self.position == 2:
            return "Member"
        else:
            return "Word Chairman"

    def __str__(self):
        return f"Candidate:{self.certificate_name} Position:{self.position_humanity()}  Symbol:{self.symbol_name.name}"


"""
def application(venv, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]
"""
