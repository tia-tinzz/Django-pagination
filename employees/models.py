from django.db import models

# Create your models here.
class Employee(models.Model):
    title = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title