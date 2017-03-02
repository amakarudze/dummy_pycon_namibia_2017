from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Entry(models.Model):
    title = models.CharField(max_length=200)
    date_posted = models.DateTimeField("date posted", default=timezone.now)
    author = models.ForeignKey(User)

    class Meta:
        managed = True
        verbose_name_plural = "entries"

    def __str__(self):
        return self.title