from django.db import models


class ToDoList(models.Model):
    CHOICES = (
        ("1", "priority1"),
        ("2", "priority2"),
        ("3", "priority3"),
        ("4", "priority4"),
    )
    task = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_data = models.DateField()
    end_data = models.DateField(blank=True)
    time = models.TimeField()
    priority = models.CharField(max_length=10, choices=CHOICES)

    def __str__(self):
        return f"task={self.task}, priority={self.priority}"
