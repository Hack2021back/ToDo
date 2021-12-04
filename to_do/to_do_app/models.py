import http

from django.db import models
from datetime import date

from django.core.validators import MaxValueValidator
from django.db import models
from rest_framework.exceptions import ValidationError
from django import forms


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

    def __str__(self):
        return f"task={self.task}, priority={self.priority}"

    class Meta:
        verbose_name = "Plans"
        verbose_name_plural = "Plans"
        ordering = ["priority", "task"]

    def save(self, *args, **kwargs):
        if self.start_data > self.end_data:
            raise ValidationError("ABOBA")
        super(ToDoList, self).save(args, **kwargs)

