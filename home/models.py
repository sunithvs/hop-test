from datetime import datetime

from django.db import models

time_slots = (
    '8:00AM-8:30AM',
    '8:30AM-9:00AM',
    '9:00AM-9:30AM',
    '9:30AM-10:00AM',
    '10:00AM-10:30AM',
    '10:30AM-11:00AM',
    '11:00AM-11:30AM',
    '11:30AM-12:00PM',
    '12:00PM-12:30PM',
    '12:30PM-1:00PM',
    '1:00PM-1:30PM',
    '1:30PM-2:00PM',
    '2:00PM-2:30PM',
    '2:30PM-3:00PM',
    '3:00PM-3:30PM',
    '3:30PM-4:00PM',
    '4:00PM-4:30PM',
    '4:30PM-5:00PM',
    '5:00PM-5:30PM',
    '5:30PM-6:00PM',
    '6:00PM-6:30PM',
    '6:30PM-7:00PM')


def validate_time_slot(slot, date):
    if slot not in time_slots:
        return False, "Invalid Time Slot"
    if date < datetime.now().date():
        return False, "Past Date cannot be selected please select future date"
    if Appointment.objects.filter(date=date,
                                  time=slot).exists():
        return False, "Slot already booked please select another slot"
    return True, "Valid Slot"


class Appointment(models.Model):
    # make time slots as intervals of 30 minutes
    user = models.ForeignKey('auth_login.User',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    date = models.DateField()
    time = models.CharField(max_length=50,
                            choices=[(slot, slot) for slot
                                     in time_slots])
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name


