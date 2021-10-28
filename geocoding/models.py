from django.db import models
import uuid


class Location(models.Model):
    point = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.point


class Task(models.Model):
    status = models.BooleanField(default=False)  # (running, done)
    task_id = models.UUIDField(default=uuid.uuid4)
