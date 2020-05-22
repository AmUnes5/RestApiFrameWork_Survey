from rest_framework import viewsets
from .serializers import etudiantSerializer
from .models import etudiant


class etudiantViewSet(viewsets.ModelViewSet):
    queryset = etudiant.objects.all()
    serializer_class = etudiantSerializer
