from django.urls import path

from app.views.homepage_view import Homepage
from app.views.dashboard_view import DashboardView
from app.views.user_view import SignInView, SingUpView, Logout
from app.views.profile_view import ProfileView, ProfileUpdateView
from app.views import nomination_view

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # user management
    path('login/', SignInView.as_view(), name='login'),
    path('signup/', SingUpView.as_view(), name='signup'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-update/<pk>/', ProfileUpdateView.as_view(), name='profile_update'),
    # nominations/candidates
    path('symbol/', nomination_view.SymbolView.as_view(), name='symbol_view'),
    path('nomination-apply/', nomination_view.NominationApplyView.as_view(), name='nomination_apply'),
    path('nomination/', nomination_view.NominationSubmitList.as_view(), name='nomination_view'),
    path('candidates-list/', nomination_view.CandidatesList.as_view(), name='candidates_list'),
    path('candidates-details/<pk>/', nomination_view.CandidatesDetails.as_view(), name='candidates_details'),
    path('candidates-update/<pk>/', nomination_view.CandidatesUpdateView.as_view(), name='candidates_update'),
    path('nomination-profile/<pk>/', nomination_view.NominationProfile.as_view(), name='nomination_profile'),
]
