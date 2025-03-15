from django.urls import path
from . import views

app_name = 'service'
urlpatterns = [
    path('service/', views.ServiceView.as_view(), name='service'),
    path('detail/<int:service_id>/', views.ServiceDetailView.as_view(), name='detail'),
]
