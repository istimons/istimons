from rest_framework import generics
from .models import SchoolSettings
from .serializers import SchoolSettingsSerializer


class SchoolSettingsView(generics.RetrieveUpdateAPIView):
    serializer_class = SchoolSettingsSerializer

    def get_object(self):
        return SchoolSettings.objects.get(school=self.request.user.school)
