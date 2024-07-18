# views.py
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models.flexiblebookings import FlexibleBooking
from core.serializers.flexiblebooking import FlexibleBookingSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class FlexibleBookingListView(APIView):
    def get(self, request):
        bookings = FlexibleBooking.objects.all()
        serializer = FlexibleBookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new flexible booking",
        request_body=FlexibleBookingSerializer,
        responses={201: FlexibleBookingSerializer, 400: 'Bad Request'}
    )
    def post(self, request):
        serializer = FlexibleBookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FlexibleBookingDetailView(APIView):
    def get_object(self, pk):
        try:
            return FlexibleBooking.objects.get(pk=pk)
        except FlexibleBooking.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        booking = self.get_object(pk)
        serializer = FlexibleBookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        booking = self.get_object(pk)
        serializer = FlexibleBookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        booking = self.get_object(pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
