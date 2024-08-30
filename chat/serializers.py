from rest_framework import serializers
from .models import Chat
from requirements.models import Requirements
from user.models import CustomUser, UserType

class ChatSerializer(serializers.ModelSerializer):
    requirements = serializers.PrimaryKeyRelatedField(queryset=Requirements.objects.all())
    seller = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(user_type=UserType.SELLER))

    class Meta:
        model = Chat
        fields = ['id', 'requirements', 'seller']

    def validate(self, attrs):
        # Validate that the requirements and seller exist
        requirements = attrs.get('requirements')
        seller = attrs.get('seller')

        if not Requirements.objects.filter(id=requirements.id).exists():
            raise serializers.ValidationError("The specified requirements do not exist.")
        
        if not CustomUser.objects.filter(id=seller.id, user_type=UserType.SELLER).exists():
            raise serializers.ValidationError("The specified seller does not exist or is not of type 'seller'.")

        return attrs

