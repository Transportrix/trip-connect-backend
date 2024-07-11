from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from core.models.bookedseats import BookedSeat
from core.models.fixedbookings import FixedBooking
from core.models.transportschedules import TransportSchedules
from core.serializers.bookedseat import BookedSeatSerializer
from core.serializers.fixedbooking import BookingsSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class BookingsList(APIView):
    def get(self, request):
        bookings = FixedBooking.objects.all()
        serializer = BookingsSerializer(bookings, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['user', 'bus_schedule', 'seat_numbers'],
            properties={
                'user': openapi.Schema(type=openapi.TYPE_INTEGER),
                'bus_schedule': openapi.Schema(type=openapi.TYPE_INTEGER),
                'seat_numbers': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_INTEGER)
                ),
            },
        ),
        responses={200: BookedSeatSerializer(many=True)},
    )    
    def post(self, request):
        try:
            user = request.data["user"]  # Assuming user authentication is set up
            bus_schedule_id = request.data['bus_schedule']  # Assuming you submit bus_schedule_id in the request data
            seat_numbers = request.data['seat_numbers']  # Assuming you submit seat_numbers as a list in the request data

            # Retrieve the bus schedule object or return 404 if not found
            bus_schedule = get_object_or_404(TransportSchedules, pk=bus_schedule_id)

            # Check if any of the seats are already booked for this bus_schedule
            already_booked_seats = BookedSeat.objects.filter(booking__bus_schedule=bus_schedule, seat_number__in=seat_numbers).values_list('seat_number', flat=True)
            if already_booked_seats:
                return Response({"error": f"These seats ({', '.join(map(str, already_booked_seats))}) are already booked for the selected bus schedule."}, status=status.HTTP_400_BAD_REQUEST)

            # Create a FixedBooking instance with user and bus_schedule
            fixed_booking = FixedBooking.objects.create(user_id=user, bus_schedule=bus_schedule)

            # Create a list of BookedSeat objects to save in bulk
            booked_seats = []
            for seat_number in seat_numbers:
                booked_seats.append(BookedSeat(booking=fixed_booking, seat_number=seat_number))

            # Bulk create BookedSeat objects
            BookedSeat.objects.bulk_create(booked_seats)

            # Retrieve all booked seats for the response
            booked_seats_queryset = BookedSeat.objects.filter(booking=fixed_booking)
            serializer = BookedSeatSerializer(booked_seats_queryset, many=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except TransportSchedules.DoesNotExist:
            return Response({"error": "Bus schedule does not exist."}, status=status.HTTP_404_NOT_FOUND)

        except KeyError as e:
            return Response({"error": f"Required field '{e.args[0]}' is missing."}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class BookingsDetail(APIView):
    def get_object(self, pk):
        try:
            return FixedBooking.objects.get(pk=pk)
        except FixedBooking.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        bookings = self.get_object(pk)
        serializer = BookingsSerializer(bookings)
        return Response(serializer.data)


    @swagger_auto_schema(request_body=BookingsSerializer)
    def put(self, request, booking_id):
        try:
            fixed_booking = get_object_or_404(FixedBooking, pk=booking_id)
            seat_data_list = request.data['seat_numbers']
            existing_booked_seats = BookedSeat.objects.filter(booking=fixed_booking)
            existing_seat_numbers = set(existing_booked_seats.values_list('seat_number', flat=True))
            new_seat_numbers = []

            for seat_number in seat_data_list:
                if seat_number in existing_seat_numbers:
                    # Check if the seat is already booked in the same FixedBooking
                    if not existing_booked_seats.filter(seat_number=seat_number).exists():
                        return Response({"error": f"Seat {seat_number} is already booked by another user for this bus schedule."}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    # Check if the seat is booked by a different FixedBooking
                    if BookedSeat.objects.filter(booking__bus_schedule=fixed_booking.bus_schedule, seat_number=seat_number).exclude(booking=fixed_booking).exists():
                        return Response({"error": f"Seat {seat_number} is already booked by another user for this bus schedule."}, status=status.HTTP_400_BAD_REQUEST)
                new_seat_numbers.append(seat_number)

            # Create or update booked seats
            for seat_number in new_seat_numbers:
                if seat_number not in existing_seat_numbers:
                    BookedSeat.objects.create(booking=fixed_booking, seat_number=seat_number)

            # Delete existing booked seats that are not in new_seat_numbers
            existing_booked_seats.exclude(seat_number__in=new_seat_numbers).delete()

            # Return updated booked seats
            updated_booked_seats = BookedSeat.objects.filter(booking=fixed_booking)
            serializer = BookedSeatSerializer(updated_booked_seats, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except FixedBooking.DoesNotExist:
            return Response({"error": "Booking does not exist."}, status=status.HTTP_404_NOT_FOUND)

        except KeyError as e:
            return Response({"error": f"Required field '{e.args[0]}' is missing."}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        bookings = self.get_object(pk)
        bookings.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
