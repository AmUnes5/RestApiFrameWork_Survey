from rest_framework import serializers
from .models import etudiant


class etudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = etudiant
        fields = '__all__'