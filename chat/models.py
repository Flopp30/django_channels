from django.db import models

from user.models import User


class Chat(models.Model):
    id = models.UUIDField(verbose_name="id", primary_key=True)
    name = models.CharField(verbose_name="name", max_length=128)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="chats", blank=True,
    )
    created_at = models.DateTimeField(verbose_name="created", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated", auto_now=True)

    def __str__(self):
        return f"{self.pk}: {self.name}({self.owner})"

    def __repr__(self):
        return f"Chat(name={self.name}, owner={self.owner})"

    class Meta:
        verbose_name = "Chat"
        verbose_name_plural = "Chats"


class Message(models.Model):
    id = models.UUIDField(verbose_name="id", primary_key=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    text = models.TextField(verbose_name="Text", max_length=256)
    created_at = models.DateTimeField(verbose_name="created", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated", auto_now=True)

    def __str__(self):
        return f"{self.text}"

    def __repr__(self):
        return f"Message(chat={self.chat}, user={self.user}, text={self.text})"

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
