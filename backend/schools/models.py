from django.db import models
from shared.models import School


class SchoolSettings(models.Model):
    school = models.OneToOneField(
        School, on_delete=models.CASCADE, related_name="settings"
    )
    logo = models.ImageField(upload_to="logos/", blank=True, null=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    motto = models.CharField(max_length=200, blank=True)
    grading_system = models.JSONField(default=dict)  # {'A': 80, 'B': 70, ...}
    academic_year_start = models.DateField()
    academic_year_end = models.DateField()
    currency = models.CharField(max_length=10, default="KES")
    timezone = models.CharField(max_length=50, default="Africa/Nairobi")

    def __str__(self):
        return f"Settings for {self.school.name}"
