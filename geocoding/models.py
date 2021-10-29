from django.db import models
import uuid


class Task(models.Model):
    #point = models.CharField(max_length=255)
    #latitude = models.FloatField()
    #longitude = models.FloatField()
    status = models.BooleanField(default=True)  # (running, done)
    task_id = models.UUIDField(default=uuid.uuid4)
    # address = models.CharField(max_length=255)
    # distance = models.FloatField() 

    def __str__(self):
        return f"{self.task_id}"


class Point(models.Model):
    """
    Results from each Task
    """
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Link(models.Model):
    """
    Results from each Task
    """
    task = models.OneToOneField(Task, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    distance = models.FloatField()


