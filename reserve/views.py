from django.shortcuts import render, redirect
from django.views import View
from .models import ReservationUser, Appointment, TypeService
from .forms import ReservationForm
from django.contrib import messages
from django.http import HttpResponse
import logging


# Create your views here.
class TypeServiceView(View):
    def get(self, request):
        services = TypeService.objects.all()
        return render(request, 'reservation/service.html', {'services': services})


class ReservationView(View):
    template_name = 'reservation/reservation.html'

    def get(self, request, service_id):
        appointments = Appointment.objects.filter(type_service_id=service_id, is_active=True)
        form = ReservationForm(initial={'service_id': service_id})
        form.fields['admin_appointment'].queryset = appointments
        return render(request, self.template_name, {'appointments': appointments, 'form': form})

    def post(self, request, service_id):
        appointments = Appointment.objects.filter(type_service_id=service_id, is_active=True)
        form = ReservationForm(request.POST)
        form.fields['admin_appointment'].queryset = appointments
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['phone_number']
            appointment = form.cleaned_data['admin_appointment']
            reservation = ReservationUser(full_name=full_name, phone_number=phone_number, admin_appointment=appointment,
                                          type_service=appointment.type_service)
            reservation.save()
            return HttpResponse('Reservation successfully created!')
        return render(request, self.template_name, {'appointments': appointments, 'form': form})
