from rest_framework import serializers
from appointment.models import Appointment, Scheduled


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('role',
                  'name',
                  'email',
                  'phone',
                  'date',
                  'start_time',
                  'end_time')


class ScheduledSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduled
        fields = ('interviewer_id',
                  'candidate_id',
                  'date',
                  'start_time',
                  'end_time')
