from django.contrib import admin
from django.urls import path, include

from .views import SensorsList, SensorView, MeasurementDetail, MeasurementView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('measurement.urls')),
    path('sensor/', SensorsList.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),
    path('measurement/', MeasurementView.as_view()),
    path('measurement/<pk>/', MeasurementDetail.as_view()),
]