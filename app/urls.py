from django.urls import path

from app.views.user_view import UserCreateAPIView

urlpatterns = [
    path('user-create/', UserCreateAPIView.as_view())
]
