from rest_framework import serializers
from rest_framework import views, status
from rest_framework.response import Response

from app.models.nomination import Nomination


class NominationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomination
        fields = '__all__'


class ListOfNominationView(views.APIView):

    def get(self, request):
        nomination = Nomination.objects.all()
        serializer = NominationSerializer(nomination, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass
