from rest_framework import serializers
from.models import Userip

class Countserializer(serializers.ModelSerializer):

    class Meta:
        model = Userip
        fields = ['count']