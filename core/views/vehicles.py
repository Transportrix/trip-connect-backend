from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from core.models.vehicles import Vehicle
from core.models.transportschedules import TransportSchedules
from core.serializers.transportschedules import TransportSchedulesSerializer
from core.serializers.vehicle import VehicleSerializer


class VehicleList(APIView):
    def get(self, request):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=VehicleSerializer)
    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehicleDetail(APIView):
    def get_object(self, pk):
        try:
            return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        vehicle = self.get_object(pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=VehicleSerializer)
    def put(self, request, pk):
        vehicle = self.get_object(pk)
        serializer = VehicleSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vehicle = self.get_object(pk)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VehicleWithSchedules(APIView):
    def get(self, request):
        vehicles = Vehicle.objects.prefetch_related("transportschedules_set").all()
        data = []
        for vehicle in vehicles:
            schedules = vehicle.transportschedules_set.all()
            schedule_serializer = TransportSchedulesSerializer(schedules, many=True)
            vehicle_serializer = VehicleSerializer(vehicle)
            data.append(
                {
                    "vehicle": vehicle_serializer.data,
                    "schedules": schedule_serializer.data,
                }
            )
        return Response(data)


class SearchVehicleWithSchedule(APIView):
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
        ).prefetch_related("transportbusesandschedules_set__vehicle")

        serializer = TransportSchedulesSerializer(schedules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
