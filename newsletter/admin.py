from django.contrib import admin

from newsletter.models import Subscriber
from newsletter.services import send_newsletter_email


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'created_at')
    search_fields = ('email',)
    list_filter = ('is_active', 'created_at')

