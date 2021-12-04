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

<<<<<<< HEAD
    def __str__(self):
        return f"task={self.task}, priority={self.priority}"
=======
    class Meta:
        verbose_name = "Plans"
        verbose_name_plural = "Plans"
        ordering = ['priority', 'task']

    def save(self, *args, **kwargs):
        if self.start_data > self.end_data:
            raise forms.ValidationError("ABOBA")
        super(ToDoList, self).save(args, **kwargs)

# class MemberRegistration(models.Model):
#     purchase_date=models.DateField(
#     helptext=('Enter the date of purchase'),
#         validators=[MaxValueValidator(limit_value=date.today)],
#         verbosename=('purchase date')
#     )
#
#     class Meta:
#         constraints = [
#             models.CheckConstraint(
#                 check=models.Q(purchase_date__lte=Now()),
#                 name='purchase_date_cannot_be_future_dated'
#             )
#         ]

>>>>>>> 39ddfe66ce2a96666510953add1717ce72b32f6a
