from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,
                                   null=True)
    date = models.DateField()
    user = models.OneToOneField(User,
                                on_delete=models.PROTECT,
                                blank=True,
                                null=True)
    is_finished = models.BooleanField()

    class Meta:
        ordering = ['-date']