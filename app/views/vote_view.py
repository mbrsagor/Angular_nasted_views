from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from app.models.nomination import Nomination


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoteListView(ListView):
    model = Nomination
    template_name = 'vote/vote.html'
    context_object_name = 'vote_list'

    def get_queryset(self):
        return Nomination.objects.filter(status=True)
