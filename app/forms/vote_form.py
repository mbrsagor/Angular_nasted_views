from django.forms import ModelForm, Select, SelectMultiple
from app.models.vote import Vote
from app.models.nomination import Nomination


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

    # def __init__(self, *args, **kwargs):
    #     nomination = Nomination.objects.get(is_approve=True)
    #     super(VoteForm, self).__init__(*args, **kwargs)
    #     self.fields['is_approve'].queryset = Vote.objects.filter(candidate=nomination)
