from rest_framework import serializers
from .models import Staff, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class StaffSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.exclude(role__isnull=True).exclude(staff__isnull=False),
        required=False,
        source="user"
    )
    user = serializers.StringRelatedField()
    user_role = serializers.SerializerMethodField()

    class Meta:
        model = Staff
        fields = '__all__'

    def get_user_role(self, obj):
        return obj.user.role if obj.user else None
