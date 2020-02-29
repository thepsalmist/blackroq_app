from django.contrib import admin
from .models import Property, Agent, Testimonial, Booking, About


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "agent", "location", "price", "listing_date")
    list_filter = ("location", "agent", "listing_date")
    search_fields = ("title", "description")
    ordering = ("listing_date",)


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "message", "occupation")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number", "booking_date")
    list_filter = ("booking_date",)


admin.site.register(About)
