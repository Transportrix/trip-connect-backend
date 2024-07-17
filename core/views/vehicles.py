
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models.vehicles import Vehicle, VehicleModel, VehicleType
from core.serializers.vehicle import VehicleSerializer

class VehicleModelListView(APIView):
    def get(self, request):
        vehicle_type = request.query_params.get('type')
        
        if vehicle_type:
            vehicle_models = VehicleModel.objects.filter(
                vehicle__type__name__exact=vehicle_type
            ).values_list('name', flat=True).distinct()
        else:
            vehicle_models = VehicleModel.objects.values_list('name', flat=True).distinct()
        
        if not vehicle_models:
            return Response({"error": "No models found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(vehicle_models, status=status.HTTP_200_OK)

class VehicleTypeListView(APIView):
    def get(self, request):
        vehicle_types = VehicleType.objects.values_list('name', flat=True).distinct()
        
        if not vehicle_types:
            return Response({"error": "No types found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(vehicle_types, status=status.HTTP_200_OK)

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