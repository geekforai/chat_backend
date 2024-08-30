from django.db import models
from user.models import CustomUser
from user.models import UserType
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(CustomUser, related_name='projects', on_delete=models.CASCADE, limit_choices_to={'user_type': UserType.COMPANY})
    name=models.CharField(max_length=100,default=None)
    projecttype = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.projecttype}: {self.description[:50]}"