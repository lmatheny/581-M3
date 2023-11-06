from django.urls import reverse
from django.db import models

#Model to populate list
class CalendarEntry(models.Model):
    date = models.DateField()
    total_time = models.DurationField()

    def get_absolute_url(self):
        return reverse('calendar-entry-detail', args=[str(self.id)])
