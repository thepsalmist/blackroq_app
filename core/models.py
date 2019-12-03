from django.db import models
from django.shortcuts import reverse


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

LOCATION_CHOICES = (
    ("KR", "Karen"),
    ("MT", "Muthaiga"),
    ("RN", "Runda"),
    ("GE", "Garden_Estate"),
    ("RU", "Ruiru"),
)


class Agent(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    photo = models.ImageField(default="default.jpeg", upload_to="Agents/%Y/%m/%d")
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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(choices=LOCATION_CHOICES, max_length=20, default="KR")
    listing_date = models.DateTimeField(auto_now_add=True)
    main_photo = models.ImageField(default="home.jpg")
    photo_1 = models.ImageField(default="home.jpg", upload_to="Property/%Y/%m/%d")
    photo_2 = models.ImageField(default="home.jpg", upload_to="Property/%Y/%m/%d")
    photo_3 = models.ImageField(default="home.jpg", upload_to="Property/%Y/%m/%d")
    photo_4 = models.ImageField(default="home.jpg", upload_to="Property/%Y/%m/%d")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10, default="SL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:property_detail", kwargs={"pk": self.pk})

