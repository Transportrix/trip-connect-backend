# core/views/transport.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from core.models.transportschedules import TransportSchedules
from core.serializers.transportschedules import TransportSchedulesSerializer


class TransportSchedulesList(APIView):
    def get(self, request):
        travelling_from = request.query_params.get("travelling_from", None)
        travelling_to = request.query_params.get("travelling_to", None)

        if travelling_from and travelling_to:
            schedules = TransportSchedules.objects.filter(
                travelling_from__icontains=travelling_from,
                travelling_to__icontains=travelling_to,
            )
            print(schedules.query)  # Print the SQL query being executed

        else:
            schedules = TransportSchedules.objects.all()

        serializer = TransportSchedulesSerializer(schedules, many=True)
        return Response(serializer.data)


class TransportSchedulesDetail(APIView):
    def get_object(self, pk):
        try:
            return TransportSchedules.objects.get(pk=pk)
        except TransportSchedules.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        schedule = self.get_object(pk)
        serializer = TransportSchedulesSerializer(schedule)
        return Response(serializer.data)


class TransportTravellingFromToList(APIView):
    def get(self, request):
        travelling_from_to = TransportSchedules.objects.values_list(
            "travelling_from", "travelling_to"
        ).distinct()

        travelling_from_set = set()
        travelling_to_set = set()

        for travelling_from, travelling_to in travelling_from_to:
            travelling_from_set.add(travelling_from)
            travelling_to_set.add(travelling_to)

        result = [
            {"travelling_from": list(travelling_from_set)},
            {"travelling_to": list(travelling_to_set)},
        ]

        return Response(result)
