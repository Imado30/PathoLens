from django.db import models

# Create your models here.
class Dataset(models.Model):
    id = models.AutoField(primary_key=True)
    mri_scan = models.FileField()


class Session(models.Model):
    id = models.AutoField(primary_key=True)
    dataset_id = models.ForeignKey()
    study_id = models.ForeignKey()
    user_id = models.ForeignKey()
    finished = models.BooleanField()
    diagnosis_id = models.ForeignKey()
    
class Study(models.Model):
    id = models.AutoField(primary_key=True)
    contained_datasets = models.ForeignKey() # TODO Add foreign key list
    associated_users = models.ForeignKey() # TODO Add foreign key list
    allowed_masks = models.JSONField()
    finished = models.BooleanField()

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    surname = models.TextField()
    mail = models.TextField() # Validate on korrekt mail
    password_hash = models.TextField() # best to give away auth to ldap server

class Diagnosis(models.Model):
    id = models.AutoField(primary_key=True)
    diagnosis_boundaries = models.JSONField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    rediagnosed_counter = models.IntegerField()