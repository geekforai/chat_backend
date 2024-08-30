from rest_framework import serializers
from requirements.models import Requirements
from project.models import Project

class RequirementsSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Requirements
        fields = ['id', 'project', 'requirements']

    def validate(self, attrs):
        # Ensure that the project exists and is a valid project
        project = attrs.get('project')
        if not Project.objects.filter(id=project.id).exists():
            raise serializers.ValidationError("The specified project does not exist.")
        
        # Ensure that only users with 'company' type can create requirements
        user = self.context['request'].user
        if user.user_type != 'Company':
            raise serializers.ValidationError("Only users with the type 'company' can create requirements.")

        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        # Ensure that the user is associated with the project (if required by your business logic)
        return super().create(validated_data)

