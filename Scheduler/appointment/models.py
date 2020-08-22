from django.db import models


class Appointment(models.Model):
    role = models.CharField(max_length=70)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    date = models.CharField(max_length=70)
    start_time = models.IntegerField()
    end_time = models.IntegerField()


class Scheduled(models.Model):
    interviewer_id = models.IntegerField()
    candidate_id = models.IntegerField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
