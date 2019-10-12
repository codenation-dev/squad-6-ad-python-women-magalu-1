from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['title',
                  'details',
                  'number_events',
                  'occurrence_date',
                  'active',
                  #environment
                  #level
                  #origin
                  #user
                 ]
        read_only_fields = ['occurrence_date', 'active']
