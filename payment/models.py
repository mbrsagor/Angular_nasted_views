from django.db import models


class Transition(models.Model):
    payment_purpose = models.CharField(max_length=100)
    transition_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transition_number = models.IntegerField(default=0, unique=True)
    created_at = models.DecimalField(auto_now_add=True)

    def __str__(self):
        return f"Payment ID: {self.id} and amount :{self.transition_amount}"
