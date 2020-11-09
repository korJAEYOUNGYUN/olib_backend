from django.shortcuts import render
from django.contrib.auth.models import User as UserModel
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from olib.apps.users.models import Borrowing
from olib.apps.users.serializers import UserSerializer, BorrowingSerializer


class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        tokens = self.get_tokens_for_user(user)
        return Response(tokens, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save()

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


class BorrowingViewSet(viewsets.ModelViewSet):
    serializer_class = BorrowingSerializer

    def get_queryset(self):
        borrowings = Borrowing.objects.all()

        user = self.request.query_params.get('user')
        is_returned = self.request.query_params.get('is_returned')

        if user:
            borrowings = borrowings.filter(user_id=user)
        if is_returned:
            borrowings = borrowings.filter(is_returned=is_returned)

        return borrowings

    def get_permissions(self):
        if self.action == 'list' or self.action == 'create' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]