
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models.vehicles import Vehicle, VehicleModel, VehicleType
from core.serializers.vehicle import VehicleModelSerializer, VehicleSerializer, VehicleTypeSerializer


class VehicleModelListView(APIView):
    def get(self, request):
        vehicle_type = request.query_params.get('type')
        
        if vehicle_type:
            vehicle_models = VehicleModel.objects.filter(
                vehicles__type__name__iexact=vehicle_type
            ).values_list('name', flat=True).distinct()
        else:
            vehicle_models = VehicleModel.objects.filter(vehicles__isnull=False).values_list('name', flat=True).distinct()
        
        if not vehicle_models:
            return Response([], status=status.HTTP_200_OK)

        vehicle_models_list = list(vehicle_models)

        
        return Response(vehicle_models_list, status=status.HTTP_200_OK)

class VehicleTypeListView(APIView):
    def get(self, request):
        vehicle_types = VehicleType.objects.filter(vehicles__isnull=False).values_list('name', flat=True).distinct()
        
        if not vehicle_types:
            return Response([], status=status.HTTP_200_OK)
        
        vehicle_types_list = list(vehicle_types)
        
        return Response(vehicle_types_list, status=status.HTTP_200_OK)

class VehicleSearchView(APIView):
    def get(self, request):
        model = request.query_params.get('model')
        type = request.query_params.get('type')

        # Create a query dictionary to filter vehicles
        query = {}
        if model:
            query['model__name__iexact'] = model
        if type:
            query['type__name__iexact'] = type

        vehicles = Vehicle.objects.filter(**query)
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)