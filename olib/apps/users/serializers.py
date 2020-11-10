from django.contrib.auth.models import User
from rest_framework import serializers

from olib.apps.libraries.serializers import BookSerializer
from olib.apps.users.models import Borrowing


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class BorrowingSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Borrowing
        fields = '__all__'