from rest_framework import serializers
from app.models.user import User


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
        )

    class Meta:
        model = User
        fields = '__all__'
