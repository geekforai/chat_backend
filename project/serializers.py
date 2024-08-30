from rest_framework import serializers
from project.models import Project
from user.models import CustomUser

from rest_framework import serializers
from .models import Project
from user.models import CustomUser

class ProjectSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(read_only=True)  # Read-only field

    class Meta:
        model = Project
        fields = ['id', 'company', 'name','projecttype', 'description']

    def validate(self, attrs):
        # Ensure the user making the request is a company
        user = self.context['request'].user
        if user.user_type != 'Company':
            raise serializers.ValidationError("Only users of type 'company' can create or update projects.")
        return attrs

    def create(self, validated_data):
        # Automatically set the company field to the logged-in user's company
        user = self.context['request'].user
        validated_data['company'] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # The company field should not be updated
        validated_data.pop('company', None)
        return super().update(instance, validated_data)

