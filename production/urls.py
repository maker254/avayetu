from django.urls import include, path
from production.views import CustomerCreateView,VehicleCreateView,import_genealogydata_to_db,VehicleDetailView
from . import views

app_name="production"
urlpatterns = [
    path('addcustomer/', CustomerCreateView.as_view(), name='addcustomer'),
    path('addvehicle/', VehicleCreateView.as_view(), name='addvehicle'),
    path('importgenealogy/', views.import_genealogydata_to_db, name="importgenealogy"),
    path('vehicledetail/<int:pk>/', VehicleDetailView.as_view(), name='vehicledetail')
]