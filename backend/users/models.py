from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    ROLE_CHOICES = [
        ("super_admin", "Super Admin"),
        ("school_owner", "School Owner"),
        ("campus_admin", "Campus Admin"),
        ("principal", "Principal"),
        ("bursar", "Bursar"),
        ("registrar", "Registrar"),
        ("teacher", "Teacher"),
        ("class_teacher", "Class Teacher"),
        ("subject_teacher", "Subject Teacher"),
        ("librarian", "Librarian"),
        ("nurse", "Nurse"),
        ("transport_manager", "Transport Manager"),
        ("hostel_manager", "Hostel Manager"),
        ("parent", "Parent"),
        ("student", "Student"),
        ("hr_manager", "HR Manager"),
        ("accountant", "Accountant"),
        ("reception", "Reception"),
        ("it_support", "IT Support"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")
    school = models.ForeignKey(
        "shared.School", on_delete=models.CASCADE, related_name="users"
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
