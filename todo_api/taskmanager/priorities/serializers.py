from rest_framework import serializers
from .models import Priority


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = '__all__'
        read_only_fields = ['updated_at', 'deleted_at', 'deleted']