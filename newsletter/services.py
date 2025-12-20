from django.core.mail import send_mail
from django.conf import settings
from .models import Subscriber


def send_newsletter_email(subject: str, message: str):
    recipients = Subscriber.objects.filter(
        is_active=True
    ).values_list('email', flat=True)

    if not recipients:
        return 0

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=list(recipients),
        fail_silently=False,
    )

    return len(recipients)
