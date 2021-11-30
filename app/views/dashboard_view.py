from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from app.models.nomination import Nomination
from app.models.user import Profile


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DashboardView, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['nomination_list'] = Nomination.objects.all()
        context['candidate_list'] = Nomination.objects.filter(status=True)
        context['citizens'] = Profile.objects.all()
        return context
