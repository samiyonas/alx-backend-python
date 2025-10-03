from django.db import models
import uuid

class user(models.Model):
    class Role(models.TextChoices):
        GUEST = "guest", "Guest"
        HOST = "host", "Host"
        ADMIN = "admin", "Admin"

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    first_name = models.CharField(null=False, max_length=200)
    last_name = models.CharField(null=False, max_length=200)
    email = models.CharField(unique=True, null=False, max_length=200)
    password_hash = models.CharField(null=False)
    phone_number = models.CharField(null=True)
    role = models.CharField(null=False, choices=Role.choices, default=Role.GUEST)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["email"])
        ]

class message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    sender_id = models.ForeignKey(
        user,
        on_delete=models.PROTECT,
        related_name="messages"
    )
    message_body = models.TextField(null=False)
    sent_at = models.DateTimeField(auto_now_add=True)

"""
conversation_id (Primary Key, UUID, Indexed)
participants_id (Foreign Key, references User(user_id)
created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
"""
class conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    participants_id = models.ForeignKey(
        user,
        on_delete=models.CASCADE,
        related_name="conversations"
    )
    created_at = models.DateTimeField(auto_now_add=True)