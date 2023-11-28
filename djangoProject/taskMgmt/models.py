from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField(null=True)
    due_time = models.TimeField(null=True)
    urgent = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    description = models.TextField(max_length=255, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
