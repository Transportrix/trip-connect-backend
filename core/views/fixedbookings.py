from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from core.models.bookedseats import BookedSeat
from core.models.fixedbookings import FixedBooking
from core.models.transportschedules import (
    TransportBusesAndSchedules,
    TransportSchedules,
)
from core.serializers.bookedseat import BookedSeatSerializer
from core.serializers.fixedbooking import BookingsSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class BookingsList(APIView):
    def get(self, request, user_id):
        bookings = FixedBooking.objects.filter(user_id= user_id).order_by("-created_at")
        serializer = BookingsSerializer(bookings, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["user", "bus_schedule_id", "seat_numbers"],
            properties={
                "user_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                "bus_schedule_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                "bus_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                "seat_numbers": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_INTEGER),
                ),
            },
        ),
        responses={200: BookedSeatSerializer(many=True)},
    )
    def post(self, request, user_id):
        try:
            bus_id = request.data.get(
                "bus_id"
            )  # Assuming you submit bus_id in the request data
            bus_schedule_id = request.data.get(
                "bus_schedule_id"
            )  # Assuming you submit bus_schedule_id in the request data
            seat_numbers = request.data.get(
                "seat_numbers", []
            )  # Assuming you submit seat_numbers as a list in the request data

            # Retrieve the bus schedule object or return 404 if not found
            transport_buses_and_schedules = get_object_or_404(
                TransportBusesAndSchedules,
                transportbus_id=bus_id,
                schedule_id=bus_schedule_id,
            )

            # Check if any of the seats are already booked for this bus schedule
            already_booked_seats = BookedSeat.objects.filter(
                booking__bus_and_schedule=transport_buses_and_schedules,
                seat_number__in=seat_numbers,
            ).values_list("seat_number", flat=True)
            if already_booked_seats:
                return Response(
                    {
                        "error": f"These seats ({', '.join(map(str, already_booked_seats))}) are already booked for the selected bus schedule."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Create a FixedBooking instance with user and bus schedule
            fixed_booking = FixedBooking.objects.create(
                user_id=user_id,
                bus_and_schedule=transport_buses_and_schedules,
            )

            # Create a list of BookedSeat objects to save in bulk
            booked_seats = [
                BookedSeat(booking=fixed_booking, seat_number=seat_number)
                for seat_number in seat_numbers
            ]

            # Bulk create BookedSeat objects
            BookedSeat.objects.bulk_create(booked_seats)

            # Retrieve all booked seats for the response
            booked_seats_queryset = BookedSeat.objects.filter(booking=fixed_booking)
            serializer = BookingsSerializer(fixed_booking)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except TransportBusesAndSchedules.DoesNotExist:
            return Response(
                {"error": "Bus and schedule combination does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )

        except KeyError as e:
            return Response(
                {"error": f"Required field '{e.args[0]}' is missing."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class BookingsDetail(APIView):
    def get_object(self, pk, user_id):
        try:
            return FixedBooking.objects.get(pk=pk, user_id=user_id)
        except FixedBooking.DoesNotExist:
            raise Http404
        
    def get(self, request, booking_id, user_id):
        bookings = self.get_object(booking_id, user_id)
        serializer = BookingsSerializer(bookings)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=BookingsSerializer)
    def put(self, request, booking_id):
        try:
            fixed_booking = get_object_or_404(FixedBooking, pk=booking_id)
            seat_data_list = request.data["seat_numbers"]
            existing_booked_seats = BookedSeat.objects.filter(booking=fixed_booking)
            existing_seat_numbers = set(
                existing_booked_seats.values_list("seat_number", flat=True)
            )
            new_seat_numbers = []

            for seat_number in seat_data_list:
                if seat_number in existing_seat_numbers:
                    # Check if the seat is already booked in the same FixedBooking
                    if not existing_booked_seats.filter(
                        seat_number=seat_number
                    ).exists():
                        return Response(
                            {
                                "error": f"Seat {seat_number} is already booked by another user for this bus schedule."
                            },
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                else:
                    # Check if the seat is booked by a different FixedBooking
                    if (
                        BookedSeat.objects.filter(
                            booking__bus_schedule=fixed_booking.bus_schedule,
                            seat_number=seat_number,
                        )
                        .exclude(booking=fixed_booking)
                        .exists()
                    ):
                        return Response(
                            {
                                "error": f"Seat {seat_number} is already booked by another user for this bus schedule."
                            },
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                new_seat_numbers.append(seat_number)

            # Create or update booked seats
            for seat_number in new_seat_numbers:
                if seat_number not in existing_seat_numbers:
                    BookedSeat.objects.create(
                        booking=fixed_booking, seat_number=seat_number
                    )

            # Delete existing booked seats that are not in new_seat_numbers
            existing_booked_seats.exclude(seat_number__in=new_seat_numbers).delete()

            # Return updated booked seats
            updated_booked_seats = BookedSeat.objects.filter(booking=fixed_booking)
            serializer = BookedSeatSerializer(updated_booked_seats, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except FixedBooking.DoesNotExist:
            return Response(
                {"error": "Booking does not exist."}, status=status.HTTP_404_NOT_FOUND
            )

        except KeyError as e:
            return Response(
                {"error": f"Required field '{e.args[0]}' is missing."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, pk):
        bookings = self.get_object(pk)
        bookings.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SetPaymentStatusView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'booking_id',
                openapi.IN_PATH,
                description="ID of the booking to update",
                type=openapi.TYPE_INTEGER,
                required=True,
            )
        ],
        responses={
            200: BookingsSerializer,
            404: "Booking not found",
        },
    )
    def post(self, request, booking_id):
        try:
            fixed_booking = get_object_or_404(FixedBooking, pk=booking_id)
            fixed_booking.is_paid = True
            fixed_booking.save()

            serializer = BookingsSerializer(fixed_booking)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except FixedBooking.DoesNotExist:
            return Response(
                {"error": "Booking does not exist."}, status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )