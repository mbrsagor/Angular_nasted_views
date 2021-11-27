from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

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


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NominationApplyView(SuccessMessageMixin, CreateView):
    model = Nomination
    form_class = NominationForm
    template_name = 'nomination/apply-nomination.html'
    success_message = 'Nomination has been send'
    success_url = '/nomination-apply/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.candidate = self.request.user.profile
        return super(NominationApplyView, self).form_valid(form)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NominationSubmitList(ListView):
    model = Nomination
    context_object_name = 'nomination'
    template_name = 'nomination/nomination_list.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Nomination.objects.all()

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return redirect(reverse_lazy("nomination_apply"))
        return super(NominationSubmitList, self).dispatch(request, *args, **kwargs)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CandidatesList(ListView):
    model = Nomination
    context_object_name = 'nomination'
    template_name = 'nomination/candidates_list.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Nomination.objects.filter(status=True)

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return redirect(reverse_lazy("nomination_apply"))
        return super(CandidatesList, self).dispatch(request, *args, **kwargs)
