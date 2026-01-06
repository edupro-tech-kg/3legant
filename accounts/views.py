from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.urls import reverse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    RegisterSerializer,
    PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer,
    build_password_reset_payload,
)


User = get_user_model()


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        data = {
            "user": {"id": user.id, "username": user.username, "email": user.email},
            "tokens": {"refresh": str(refresh), "access": str(refresh.access_token)},
        }
        return Response(data, status=status.HTTP_201_CREATED)


class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        user = User.objects.get(email__iexact=email)

        uid, token = build_password_reset_payload(user)
        reset_path = reverse("accounts:password-reset-confirm")
        reset_link = request.build_absolute_uri(f"{reset_path}?uid={uid}&token={token}")

        send_mail(
            subject="Password reset",
            message=f"Use the following link to reset your password: {reset_link}",
            from_email=None,
            recipient_list=[email],
        )

        return Response(
            {
                "detail": "Password reset instructions sent.",
                "uid": uid,
                "token": token,
            },
            status=status.HTTP_200_OK,
        )


class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Password has been reset."}, status=status.HTTP_200_OK)

