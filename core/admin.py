from django.contrib import admin

from core.models.bookedseats import BookedSeat
from core.models.busschedules import BusSchedule
from core.models.drivers import Driver
from core.models.fixedbookings import FixedBooking
from core.models.notifications import Notification
from core.models.transportbuses import TransportBus
from core.models.users import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_at', 'updated_at')
    search_fields = ('username', 'email')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ( 'license_number', 'driving_experience', 'created_at', 'updated_at')
    search_fields = ('user__username', 'license_number')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(TransportBus)
class TransportBusAdmin(admin.ModelAdmin):
    list_display = ('bus_number', 'capacity', 'model', 'driver', 'created_at', 'updated_at')
    list_filter = ('driver',)
    search_fields = ('bus_number', 'model')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(BusSchedule)
class BusScheduleAdmin(admin.ModelAdmin):
    list_display = ('bus', 'travelling_from', 'travelling_to', 'departure_time', 'estimated_arrival_time', 'created_at', 'updated_at')
    list_filter = ('bus__driver',)
    search_fields = ('travelling_from', 'travelling_to')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(FixedBooking)
class FixedBookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'bus_schedule', 'booking_date', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'bus_schedule__bus__bus_number')
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
