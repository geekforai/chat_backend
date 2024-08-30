from django.db import models
from project.models import Project
class Requirements(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, related_name='requirements', on_delete=models.CASCADE)
    requirements = models.TextField()

    def __str__(self):
        return f"Requirements for Project ID {self.project.id}"
