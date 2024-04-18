from django.db import models


class Organizer(models.Model):
    """Organizer model."""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    organization = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    """Event model."""

    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(
        Organizer, on_delete=models.CASCADE, related_name="events"
    )
    image = models.ForeignKey("Image", on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Attendee(models.Model):
    """Attendee model."""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="attendees")

    def __str__(self):
        return self.name


class Ticket(models.Model):
    """Ticket model."""

    TICKET_TYPES = [
        ("Regular", "Regular"),
        ("VIP", "VIP"),
        ("Premium", "Premium"),
    ]
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="tickets")
    attendee = models.ForeignKey(
        Attendee, on_delete=models.CASCADE, related_name="tickets"
    )
    ticket_type = models.CharField(max_length=20, choices=TICKET_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    purchase_date = models.DateTimeField()
    is_paid = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ticket_type} Ticket for {self.event.title}"


class Image(models.Model):
    """Image model."""

    def event_image_upload(instance, filename):
        return f"event_image/{instance.event.title}/{filename}"

    image = models.ImageField(
        upload_to=event_image_upload,
        height_field=None,
        width_field=None,
        max_length=None,
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return self.event.title
