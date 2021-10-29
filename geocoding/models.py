from django.db import models
import uuid


class Task(models.Model):
    point = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.BooleanField()  # (running, done)
    task_id = models.UUIDField(default=uuid.uuid4)
    address = models.CharField(max_length=255)
    distance = models.FloatField() 

    def __str__(self):
        return self.task_id
