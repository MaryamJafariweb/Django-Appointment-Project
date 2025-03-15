from django.shortcuts import render
from django.views import View
from .models import Service


# Create your views here.

class ServiceView(View):

    def get(self, request):
        service = Service.objects.all()
        return render(request, 'service/service.html',
                      {'service': service})


class ServiceDetailView(View):
    def get(self, request, service_id):
        service = Service.objects.get(id=service_id)
        return render(request, 'service/detail.html', {'service': service})
