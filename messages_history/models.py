from django.db import models
from chat.models import Chat
class MessagesHistory(models.Model):
    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    seller_message = models.TextField()
    bot_message = models.TextField()

    def __str__(self):
        return f"Message ID {self.id}"