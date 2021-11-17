from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.serializers.user_serializer import UserCreateSerializer
from app.models.user import User


class UserCreateAPIView(views.APIView):

    def post(self, request):
        pass
