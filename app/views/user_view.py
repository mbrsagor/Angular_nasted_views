from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.serializers.user_serializer import UserCreateSerializer
from app.models.user import User


class UserCreateAPIView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer
