from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

from app.models.nomination import Nomination
from app.models.vote import Vote
from app.forms.vote_form import VoteForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoteListView(ListView):
    model = Nomination
    template_name = 'vote/vote.html'
    context_object_name = 'vote_list'

    def get_queryset(self):
        return Nomination.objects.filter(status=True)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AddVoteCrateView(SuccessMessageMixin, CreateView):
    model = Vote
    form_class = VoteForm
    template_name = 'vote/add_vote.html'
    success_message = 'Your vote has been completed'
    success_url = '/add-vote/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.citizen = self.request.user.profile
        return super(AddVoteCrateView, self).form_valid(form)
