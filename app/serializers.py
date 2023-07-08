from rest_framework import serializers

from app.models import *
class FreedomFightersMS(serializers.ModelSerializer):
    class Meta:
        model=FreedomFighters
        fields="__all__"