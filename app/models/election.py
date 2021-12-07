from django.db import models
from django.core.validators import MaxValueValidator
from app.models.user import Profile
from app.models.nomination import Nomination


class Election(models.Model):
    citizen = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='public')
    candidate = models.ForeignKey(Nomination, on_delete=models.CASCADE, related_name='election_candidate')
    created = models.DateTimeField(auto_now_add=True)
    vote = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1)])
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.citizen.user.username
