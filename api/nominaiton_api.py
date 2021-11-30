from rest_framework import serializers
from rest_framework import views, status
from rest_framework.response import Response

from app.models.nomination import Nomination, Symbol


class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        fields = (
            'id', 'name'
        )


class SymbolListAPIView(views.APIView):

    def get(self, request):
        symbol = Symbol.objects.all()
        serializer = SymbolSerializer(symbol, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SymbolSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
