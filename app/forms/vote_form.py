from django.forms import ModelForm, Select, SelectMultiple
from app.models.vote import Vote


class VoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = (
            '__all__'
        )
        exclude = ['citizen', 'citizen_id']

        widgets = {
            'candidate': SelectMultiple(attrs={'class': 'prompt', 'id': 'candidate'}),
            'vote': Select(attrs={'class': 'form-control', 'id': 'vote'}),
        }
