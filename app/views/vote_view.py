from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from app.models.vote import Vote


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoteListCreateView(ListView):
    model = Vote
    template_name = 'vote/vote.html'
    context_object_name = 'vote_list'

