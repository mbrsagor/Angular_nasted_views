from django.views.generic import ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse

from app.models.user import Profile
from app.forms.profile_form import ProfileForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfileView(ListView):
    model = Profile
    template_name = 'profile/profile.html'
    context_object_name = 'profile_ctx'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Profile.objects.get(user=self.request.user)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'profile/profile_update.html'
    success_message = "Profile has been successfully updated!"
    model = Profile
    form_class = ProfileForm

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user.id)

    def get_success_url(self):
        return reverse('profile_update', kwargs={
            'pk': self.object.pk,
        })
