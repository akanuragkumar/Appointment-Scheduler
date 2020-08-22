from django.db import models


class Appointment(models.Model):
    role = models.CharField(max_length=70)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    date = models.CharField(max_length=70, null=True)
    start_time = models.CharField(max_length=70, null=True)
    end_time = models.CharField(max_length=70, null=True)


class Scheduled(models.Model):
    interviewer_id = models.IntegerField()
    candidate_id = models.IntegerField()
    start_time = models.IntegerField(null=True)
    end_time = models.IntegerField(null=True)
