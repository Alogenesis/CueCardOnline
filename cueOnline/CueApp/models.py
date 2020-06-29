from django.db import models

# Create your models here.
# Shop request form to programmer add a template for shop cue
class Company(models.Model):
    company_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    requirement = models.TextField()

# Current Cue Control by admin
class Cue(models.Model):
    cue_type = models.CharField(max_length=60)
    cue_number = models.IntegerField()

class Current_Cue_A(models.Model):
    cue_type = models.CharField(max_length=60)
    cue_number = models.IntegerField()

class Current_Cue_B(models.Model):
    cue_type = models.CharField(max_length=60)
    cue_number = models.IntegerField()

class Current_Cue_C(models.Model):
    cue_type = models.CharField(max_length=60)
    cue_number = models.IntegerField()

# For Cue button choose
class Press_cue_A(models.Model):
    cue_type = models.CharField(max_length=60)

class Press_cue_B(models.Model):
    cue_type = models.CharField(max_length=60)

class Press_cue_C(models.Model):
    cue_type = models.CharField(max_length=60)


