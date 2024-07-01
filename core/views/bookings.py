from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from core.models.bookings import Booking
from core.serializers.bookings import BookingsSerializer

class BookingsList(APIView):
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingsSerializer(bookings, many=True)
        return  Response(serializer.data)
      
    @swagger_auto_schema(request_body=BookingsSerializer)
    def post (self, request):
        serializer = BookingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BookingsDetail(APIView):
    def get_object(self, pk):
        try:
            return Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        bookings = self.get_object(pk)
        serializer = BookingsSerializer(bookings)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=BookingsSerializer)
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = BookingsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bookings = self.get_object(pk)
        bookings.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
