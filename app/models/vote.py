from django.db import models
from app.models.user import Profile
from app.models.nomination import Nomination


class Vote(models.Model):
    citizen = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='public')
    candidate = models.ManyToManyField(Nomination, related_name='election_candidate')
    created = models.DateTimeField(auto_now_add=True)
    YES = 1
    NO = 2
    CHOICES_VOTE = (
        (YES, 'Yes Vot'),
        (NO, 'No Vot'),
    )
    vote = models.PositiveSmallIntegerField(choices=CHOICES_VOTE)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return u", ".join([a.name for a in self.candidate.allI()])

    def __str__(self):
        return self.citizen.user.username
