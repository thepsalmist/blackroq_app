from django.urls import path
from . import views
from .views import (
    property_for_sale,
    PropertyDetailView,
    book_property,
    AboutUsView,
)

app_name = "core"

urlpatterns = [
    path("", views.index, name="home"),
    path("property_for_sale/", views.property_for_sale, name="property_sale"),
    path("property/<int:pk>", PropertyDetailView.as_view(), name="property_detail"),
    path("contact/", views.contact, name="contact"),
    path("booking/", views.book_property, name="book_property"),
    path("about/", AboutUsView.as_view(), name="about_us"),
    path("search/", views.search, name="search"),
]
