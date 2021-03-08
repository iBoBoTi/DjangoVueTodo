from django.db import models

# Create your models here.
class TodoTask(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'TodoTasks'

    def __str__(self):
        return self.name

    