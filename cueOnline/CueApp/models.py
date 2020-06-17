from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    requirement = models.TextField()

class Cue(models.Model):
    cue_type = models.CharField(max_length=60)
    cue_number = models.IntegerField()


