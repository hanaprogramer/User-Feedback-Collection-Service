from django.db import models
from django.conf import settings
class Feedback(models.Model):
    CATEGORY_CHOICES = [
        ("bug", 'BUG '),
        ('feature', 'FEATURE'),
        ('general', 'GENERAL'),
    ]

    STATUS_CHOICES = [
        ('new', 'NEW'),
        ('reviewed', 'REVIEWED')
    ]
    subject = models.CharField(max_length=100)
    message = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="feedbacks"
)
    def __str__(self):
        return self.subject
    