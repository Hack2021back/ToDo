from django.contrib.auth.models import User
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
    end_data = models.DateField(blank=True)
    start_data = models.DateField()
    time = models.TimeField()
    priority = models.CharField(max_length=10, choices=CHOICES)
    user = models.ForeignKey(
        User, related_name="user", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f"task={self.task}, priority={self.priority}"

    class Meta:
        verbose_name = "Plans"
        verbose_name_plural = "Plans"
        ordering = ["priority", "task"]
