from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    arrival_date = models.DateField()
    departure_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.email})"


class Experience(models.Model):
    SERVICE_CHOICES = [
        ('ROOM', 'Room Service'),
        ('DINING', 'Dining'),
        ('SPA', 'Spa'),
        ('RECEPTION', 'Reception'),
    ]
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='experiences')
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    date = models.DateField()
    rating = models.PositiveSmallIntegerField(help_text="Rate from 1 (poor) to 5 (excellent)")
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_service_type_display()} for {self.guest.name} on {self.date}"


class Review(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='reviews')
    overall_rating = models.PositiveSmallIntegerField(help_text="Overall experience rating (1-5)")
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.guest.name} - Rating: {self.overall_rating}"
