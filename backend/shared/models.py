from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)
    subdomain = models.CharField(max_length=100, unique=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
