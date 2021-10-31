from django.db import models
import uuid


class Task(models.Model):
    task_id = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return f"{self.task_id}"


class Point(models.Model):
    """
    Results from each Task
    """
    task_id = models.ForeignKey(
        Task, 
        related_name='points',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Link(models.Model):
    """
    Results from each Task
    """
    task_id = models.ForeignKey(
        Task,
        related_name='links',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    distance = models.FloatField()

    def __str__(self):
        return self.name
