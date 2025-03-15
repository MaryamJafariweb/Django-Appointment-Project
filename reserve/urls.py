from django.urls import path
from . import views

app_name = 'reserve'
urlpatterns = [
    path('typeservice/', views.TypeServiceView.as_view(), name='typeservice'),
    path('reservation/<int:service_id>/', views.ReservationView.as_view(), name='reservation'),
]