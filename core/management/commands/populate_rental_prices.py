# core/management/commands/populate_rental_prices.py

import random
from django.core.management.base import BaseCommand
from core.models import Vehicle

class Command(BaseCommand):
    help = 'Populate rental prices for all vehicles with random values'

    def handle(self, *args, **kwargs):
        vehicles = Vehicle.objects.all()
        for vehicle in vehicles:
            vehicle.rental_price = round(random.uniform(50.0, 500.0), 2)  # Random price between 50 and 500
            vehicle.save()
            self.stdout.write(self.style.SUCCESS(f'Updated Vehicle ID {vehicle.id} with rental price {vehicle.rental_price}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated rental prices for all vehicles'))
