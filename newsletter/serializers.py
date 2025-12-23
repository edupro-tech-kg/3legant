from rest_framework import serializers
from .models import Subscriber


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('email',)

    def validate_email(self, value):
        if Subscriber.objects.filter(email=value, is_active=True).exists():
            raise serializers.ValidationError("Email already subscribed")
        return value


class SendNewsletterSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=255)
    message = serializers.CharField()
