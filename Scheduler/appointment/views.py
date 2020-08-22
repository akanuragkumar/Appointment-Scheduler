from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from appointment.models import Appointment, Scheduled
from appointment.serializers import AppointmentSerializer, ScheduledSerializer
from rest_framework.decorators import api_view


@api_view(['POST', 'PUT', 'DELETE'])
def appointment(request):
    """This Endpoint takes the candidate/interview details and their available time-slot"""
    if request.method == 'POST':
        appointment_data = JSONParser().parse(request)
        appointment_serializer = AppointmentSerializer(data=appointment_data)
        if appointment_serializer.is_valid():
            appointment_serializer.save()
            return JsonResponse(appointment_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            data = JSONParser().parse(request)
            appointment_delete = Appointment.objects.get(id=data['id'])
        except Appointment.DoesNotExist:
            return JsonResponse({'message': 'The appointment does not exist'}, status=status.HTTP_404_NOT_FOUND)
        appointment_delete.delete()
        return JsonResponse({'message': 'appointment was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        try:
            appointment_data = JSONParser().parse(request)
            appointment_find = Appointment.objects.get(id=appointment_data['id'])
        except Appointment.DoesNotExist:
            return JsonResponse({'message': 'The appointment does not exist'}, status=status.HTTP_404_NOT_FOUND)
        del appointment_data['id']
        appointment_serializer = AppointmentSerializer(appointment_find, data=appointment_data)
        if appointment_serializer.is_valid():
            appointment_serializer.save()
            return JsonResponse(appointment_serializer.data)
        return JsonResponse(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def appointment_match(request):
    """This Endpoint returns candidate_id, interviewer_id and their matching time-slots"""
    try:
        interviewer_id = request.GET["interviewer_id"]
        candidate_id = request.GET["candidate_id"]
        interviewer = Appointment.objects.get(id=interviewer_id)
        candidate = Appointment.objects.get(id=candidate_id)
    except Appointment.DoesNotExist:
        return JsonResponse({'message': 'The appointment does not exist'}, status=status.HTTP_404_NOT_FOUND)
    interviewer_slot = range(int(interviewer.start_time), int(interviewer.end_time))
    candidate_slot = range(int(candidate.start_time), int(candidate.end_time))
    x_interviewer = set(interviewer_slot)
    slot = x_interviewer.intersection(candidate_slot)
    slots_start = []
    slots_end = []
    for x in slot:
        slots_start.append(x)
    for x in slot:
        slots_end.append(x+1)
    slots = list(zip(slots_start, slots_end))
    return JsonResponse({'Matching Slots': slots}, status=status.HTTP_200_OK)


@api_view(['POST', 'PUT', 'DELETE', 'GET'])
def scheduled(request):
    """This Endpoint takes candidate_id, interviewer_id and their preferred matching time-slots"""
    if request.method == 'POST':
        scheduled_data = JSONParser().parse(request)
        scheduled_serializer = ScheduledSerializer(data=scheduled_data)
        if scheduled_serializer.is_valid():
            scheduled_serializer.save()
            return JsonResponse(scheduled_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(scheduled_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            data = JSONParser().parse(request)
            scheduled_delete = Scheduled.objects.get(id=data['id'])
        except Scheduled.DoesNotExist:
            return JsonResponse({'message': 'The appointment does not exist'}, status=status.HTTP_404_NOT_FOUND)
        scheduled_delete.delete()
        return JsonResponse({'message': 'appointment was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        try:
            scheduled_data = JSONParser().parse(request)
            scheduled_find = Scheduled.objects.get(id=scheduled_data['id'])
        except Scheduled.DoesNotExist:
            return JsonResponse({'message': 'The appointment does not exist'}, status=status.HTTP_404_NOT_FOUND)
        del scheduled_data['id']
        scheduled_serializer = ScheduledSerializer(scheduled_find, data=scheduled_data)
        if scheduled_serializer.is_valid():
            scheduled_serializer.save()
            return JsonResponse(scheduled_serializer.data)
        return JsonResponse(scheduled_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        scheduled = Scheduled.objects.all()
        scheduled_serializer = ScheduledSerializer(scheduled, many=True)
        return JsonResponse(scheduled_serializer.data, safe=False)
