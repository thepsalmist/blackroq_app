from django.db import models
from django.shortcuts import reverse
from cloudinary.models import CloudinaryField


BEDROOM_CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8"),
)
CATEGORY_CHOICES = (
    ("SL", "Sale"),
    ("RE", "Rent"),
)


class Agent(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    photo = CloudinaryField("photo")
    description = models.TextField(blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Property(models.Model):
    title = models.CharField(max_length=100)
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING, null=True)
    area = models.FloatField()
    bedroom = models.IntegerField(choices=BEDROOM_CHOICES, default=1)
    bathroom = models.IntegerField(default=1)
    garage = models.IntegerField(default=1)
    description = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=50, default="MALINDI")
    listing_date = models.DateTimeField(auto_now_add=True)
    main_photo = CloudinaryField(default="blackroq_3.jpg")
    photo_1 = CloudinaryField("photo_1")
    photo_2 = CloudinaryField("photo_2", blank=True)
    photo_3 = CloudinaryField("photo_3", blank=True)
    photo_4 = CloudinaryField("photo_4", blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10, default="SL")

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:property_detail", kwargs={"pk": self.pk})


class Testimonial(models.Model):
    message = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message by {self.name}"


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, blank=False)
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title
