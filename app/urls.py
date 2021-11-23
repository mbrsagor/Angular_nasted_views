from django.urls import path

from app.views.homepage_view import Homepage
from app.views.dashboard_view import DashboardView
from app.views.user_view import SignInView, SingUpView, Logout
from app.views.profile_view import ProfileView, ProfileUpdateView
from app.views.nomination_view import SymbolView

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # user management
    path('login/', SignInView.as_view(), name='login'),
    path('signup/', SingUpView.as_view(), name='signup'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-update/<pk>/', ProfileUpdateView.as_view(), name='profile_update'),
    # nomination
    path('symbol/', SymbolView.as_view(), name='symbol_view'),
]
