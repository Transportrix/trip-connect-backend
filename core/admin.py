from django.contrib import admin
from core.models.bookedseats import BookedSeat
from core.models.flexiblebookings import FlexibleBooking
from core.models.transportbus import TransportBus
from core.models.transportschedules import (
    TransportSchedules,
    TransportBusesAndSchedules,
)
from core.models.drivers import Driver
from core.models.fixedbookings import FixedBooking
from core.models.notifications import Notification
from core.models.vehicleimage import VehicleImage
from core.models.vehicles import Vehicle, VehicleModel, VehicleType
from core.models.users import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("username", "email")
    readonly_fields = ("created_at", "updated_at")
    list_display = ("username", "email", "created_at", "updated_at")
    # list_filter = ('is_active', 'is_staff')


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("license_number", "user", "created_at", "updated_at")
    search_fields = ("user__username", "license_number")
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("created_at", "updated_at")


@admin.register(FixedBooking)
class FixedBookingAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "bus_and_schedule",
        "booking_date",
        "status",
        "created_at",
        "updated_at",
    )
    list_filter = ("status", "booking_date")
    search_fields = (
        "user__username",
        "bus_and_schedule__schedule__travelling_from",
        "bus_and_schedule__schedule__travelling_to",
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(BookedSeat)
class BookedSeatAdmin(admin.ModelAdmin):
    list_display = ("booking", "seat_number", "created_at", "updated_at")
    search_fields = ("booking__user__username",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "subject",
        "message",
        "type",
        "status",
        "created_at",
        "updated_at",
    )
    list_filter = ("type", "status")
    search_fields = ("user__username", "subject")
    readonly_fields = ("created_at", "updated_at")


@admin.register(TransportBusesAndSchedules)
class TransportBusesAndSchedulesAdmin(admin.ModelAdmin):
    list_display = ("schedule", "transportbus", "created_at", "updated_at")
    # search_fields = ('schedule__travelling_from', 'schedule__travelling_to', 'vehicle__vehicle_number')
    readonly_fields = ("created_at", "updated_at")


class TransportBusesAndSchedulesInline(admin.TabularInline):
    model = TransportBusesAndSchedules
    extra = 1


@admin.register(TransportSchedules)
class TransportSchedulesAdmin(admin.ModelAdmin):
    inlines = [TransportBusesAndSchedulesInline]


@admin.register(TransportBus)
class TransportBusAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


@admin.register(FlexibleBooking)
class FlexibleBookingAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]


class VehicleImageInline(admin.TabularInline):
    model = VehicleImage
    extra = 1  # Number of inline forms to display

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    inlines = [VehicleImageInline]


admin.site.register(VehicleModel)
admin.site.register(VehicleType)