from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse

from app.models.nomination import Symbol, Nomination
from app.forms.nomination_form import SymbolForm, NominationForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SymbolView(SuccessMessageMixin, CreateView, ListView):
    model = Symbol
    form_class = SymbolForm
    success_message = 'Symbol has been created'
    template_name = 'symbol/symbol.html'
    success_url = '/symbol/'
    context_object_name = 'symbol'
    paginate_by = 6
