from django.db import models

# Create your models here.
class JobVacations(models.Model):
    name = models.CharField(max_length=25, blank=True)
    places = models.CharField(max_length=50, blank=True)
    information = models.TextField()
    salary = models.IntegerField()

    def __str__(self):
        return self.name

