from django.contrib import admin
from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("subject", "category", "status", "owner", "created_at")
    list_filter = ("category", "status")
    search_fields = ("subject", "message")
