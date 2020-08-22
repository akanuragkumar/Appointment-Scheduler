from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Appointment(models.Model):
    role = models.CharField(max_length=70)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    date = models.CharField(max_length=70)
    start_time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(23)])
    end_time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(23)])


class Scheduled(models.Model):
    interviewer_id = models.IntegerField()
    candidate_id = models.IntegerField()
    start_time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(23)])
    end_time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(23)])
