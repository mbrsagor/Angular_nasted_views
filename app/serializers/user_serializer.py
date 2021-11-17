from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from app.models.user import User


class UserCreateSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(max_length=50, allow_blank=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'full_name', 'phone_number', 'gender', 'education', 'address', 'union_name',
            'nid', 'age', 'date_of_birth', 'profile_picture', 'password', 'password2'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            phone_number=validated_data['phone_number'],
            gender=validated_data['gender'],
            education=validated_data['education'],
            address=validated_data['address'],
            union_name=validated_data['union_name'],
            nid=validated_data['nid'],
            age=validated_data['age'],
            date_of_birth=validated_data['date_of_birth'],
            profile_picture=validated_data['profile_picture']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
