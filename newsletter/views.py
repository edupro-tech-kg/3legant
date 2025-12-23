from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import Subscriber
from .serializers import (
    SubscribeSerializer,
    SendNewsletterSerializer
)
from .services import send_newsletter_email


class SubscribeView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = SubscribeSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']

            subscriber, created = Subscriber.objects.get_or_create(
                email=email
            )
            subscriber.is_active = True
            subscriber.save()

            return Response(
                {"detail": "Subscribed successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnsubscribeView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')

        try:
            subscriber = Subscriber.objects.get(email=email)
            subscriber.is_active = False
            subscriber.save()
            return Response({"detail": "Unsubscribed"})
        except Subscriber.DoesNotExist:
            return Response(
                {"detail": "Email not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class SendNewsletterView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = SendNewsletterSerializer(data=request.data)
        if serializer.is_valid():
            count = send_newsletter_email(
                subject=serializer.validated_data['subject'],
                message=serializer.validated_data['message']
            )

            return Response(
                {"detail": f"Newsletter sent to {count} subscribers"},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
