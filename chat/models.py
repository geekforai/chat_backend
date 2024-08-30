from django.db import models
from requirements.models import Requirements
from user.models import CustomUser
from user.models import UserType
class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    requirements = models.ForeignKey(Requirements, related_name='chats', on_delete=models.CASCADE)
    seller = models.ForeignKey(CustomUser, related_name='chats', on_delete=models.CASCADE, limit_choices_to={'user_type': UserType.SELLER})

    def __str__(self):
        return f"Chat ID {self.id}"
