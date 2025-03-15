from django.urls import path
from . import views

app_name = 'education'
urlpatterns = [
    path('list/', views.EducationListView.as_view(), name='education_list'),
    path('detail/<int:education_id>/<slug:education_slug>/', views.DetailEducationView.as_view(),
         name='education_detail'),
]
