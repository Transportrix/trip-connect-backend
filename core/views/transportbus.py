from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from core.models.transportbus import TransportBus
from core.models.transportschedules import (
    TransportBusesAndSchedules,
    TransportSchedules,
)
from core.serializers.transportschedules import (
    TransportBusesAndSchedulesSerializer,
    TransportSchedulesSerializer,
    TransportSchedulesWithBusesSerializer,
)
from core.serializers.vehicle import TransportBusSerializer


class TransportBusList(APIView):
    def get(self, request):
        TransportBuss = TransportBus.objects.all()
        serializer = TransportBusSerializer(TransportBuss, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TransportBusSerializer)
    def post(self, request):
        serializer = TransportBusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransportBusDetail(APIView):
    def get_object(self, pk):
        try:
            return TransportBus.objects.get(pk=pk)
        except TransportBus.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        TransportBus = self.get_object(pk)
        serializer = TransportBusSerializer(TransportBus)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TransportBusSerializer)
    def put(self, request, pk):
        TransportBus = self.get_object(pk)
        serializer = TransportBusSerializer(TransportBus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        TransportBus = self.get_object(pk)
        TransportBus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TransportBusWithSchedules(APIView):
    def get(self, request):
        travelling_from = request.query_params.get("travelling_from")
        travelling_to = request.query_params.get("travelling_to")

        schedules = TransportSchedules.objects.prefetch_related(
            "transportbusesandschedules_set__transportbus"
        )

        if travelling_from and travelling_to:
            schedules = schedules.filter(
                travelling_from=travelling_from, travelling_to=travelling_to
            )

        serializer = TransportSchedulesWithBusesSerializer(schedules, many=True)
        return Response(serializer.data)


class SearchTransportBusWithSchedule(APIView):
    def get(self, request):
        travelling_from = request.query_params.get("travelling_from")
        travelling_to = request.query_params.get("travelling_to")

        if not travelling_from or not travelling_to:
            return Response(
                {
                    "error": "Both 'travelling_from' and 'travelling_to' parameters are required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        schedules = TransportSchedules.objects.filter(
            travelling_from=travelling_from, travelling_to=travelling_to
        ).prefetch_related("transportbusesandschedules_set__TransportBus")

        serializer = TransportSchedulesSerializer(schedules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
