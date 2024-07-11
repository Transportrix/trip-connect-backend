from django.contrib import admin

from core.models.bookedseats import BookedSeat
from core.models.transportschedules import TransportSchedules, TransportBusesAndSchedules
from core.models.drivers import Driver
from core.models.fixedbookings import FixedBooking
from core.models.notifications import Notification
from core.models.vehicles import Vehicle
from core.models.users import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('username', 'email')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('license_number', 'created_at', 'updated_at')
    search_fields = ('user__username', 'license_number')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Vehicle)
class VehiclesAdmin(admin.ModelAdmin):
    list_display = ('vehicle_number', 'capacity', 'model', 'driver', 'created_at', 'updated_at')
    list_filter = ('driver',)
    search_fields = ('vehicle_number', 'model')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(TransportSchedules)
class TransportSchedulesAdmin(admin.ModelAdmin):
    list_display = ('travelling_from', 'travelling_to', 'departure_time', 'estimated_arrival_time', 'created_at', 'updated_at')
    search_fields = ('travelling_from', 'travelling_to')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(FixedBooking)
class FixedBookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'bus_schedule', 'booking_date', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'bus_schedule__travelling_from', 'bus_schedule__travelling_to')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(BookedSeat)
class BookedSeatAdmin(admin.ModelAdmin):
    list_display = ('booking', 'seat_number', 'created_at', 'updated_at')
    search_fields = ('booking__user__username',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'message', 'type', 'status', 'created_at', 'updated_at')
    list_filter = ('type', 'status')
    search_fields = ('user__username', 'subject')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(TransportBusesAndSchedules)
class TransportBusesAndSchedulesAdmin(admin.ModelAdmin):
    list_display = ('schedule', 'vehicle', 'created_at', 'updated_at')
    search_fields = ('schedule__travelling_from', 'schedule__travelling_to', 'vehicle__vehicle_number')
    readonly_fields = ('created_at', 'updated_at')
