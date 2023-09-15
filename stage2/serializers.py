from rest_framework import serializers
# from django.contrib.auth import User
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Person
        fields = ['name', 'track']