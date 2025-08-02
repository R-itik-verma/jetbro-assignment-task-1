from rest_framework import serializers
from .models import Essay, EssayVersion

class EssaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Essay
        fields = '__all__'
                
class EssayVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EssayVersion
        fields = '__all__'
        read_only_fields = ['scorecard', 'submitted_at']
