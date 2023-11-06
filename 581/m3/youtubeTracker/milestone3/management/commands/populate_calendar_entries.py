from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from milestone3.models import CalendarEntry

class Command(BaseCommand):
    help = 'Populate CalendarEntry records'

    def handle(self, *args, **kwargs):
        # Create 10 entries with different dates and times
        entry1 = CalendarEntry(date='2023-11-01', total_time=timedelta(hours=7, minutes=55))
        entry1.save()

        entry2 = CalendarEntry(date='2023-11-02', total_time=timedelta(hours=8, minutes=30))
        entry2.save()

        entry3 = CalendarEntry(date='2023-11-03', total_time=timedelta(hours=7, minutes=45))
        entry3.save()

        entry4 = CalendarEntry(date='2023-11-04', total_time=timedelta(hours=8, minutes=15))
        entry4.save()

        entry5 = CalendarEntry(date='2023-11-05', total_time=timedelta(hours=9, minutes=30))
        entry5.save()

        entry6 = CalendarEntry(date='2023-11-06', total_time=timedelta(hours=7, minutes=20))
        entry6.save()

        entry7 = CalendarEntry(date='2023-11-07', total_time=timedelta(hours=8, minutes=50))
        entry7.save()

        entry8 = CalendarEntry(date='2023-11-08', total_time=timedelta(hours=6, minutes=10))
        entry8.save()

        entry9 = CalendarEntry(date='2023-11-09', total_time=timedelta(hours=10, minutes=5))
        entry9.save()

        entry10 = CalendarEntry(date='2023-11-10', total_time=timedelta(hours=7, minutes=40))
        entry10.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated 10 CalendarEntry records'))
