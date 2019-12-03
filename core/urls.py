from django.urls import path
from . import views
from .views import propertyForRent, propertyForSale, PropertyDetailView

app_name = "core"

urlpatterns = [
    path("", views.index, name="home"),
    path("property_for_rent/", views.propertyForRent, name="property_rent"),
    path("property_for_sale/", views.propertyForSale, name="property_sale"),
    path("property/<int:pk>", PropertyDetailView.as_view(), name="property_detail"),
    path("contact/", views.contact, name="contact"),
]
