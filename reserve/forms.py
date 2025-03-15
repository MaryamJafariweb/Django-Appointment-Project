from django import forms
from .models import ReservationUser, TypeService,Appointment
from jdatetime import datetime as jdatetime
from extensions.utils import jalali_converter


class ReservationForm(forms.ModelForm):

    class Meta:
        model = ReservationUser
        fields = ['full_name', 'phone_number', 'admin_appointment']


