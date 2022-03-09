from .models import Company, Office, Service
from django.contrib.auth.models import User
from rest_framework import serializers, validators

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', "created_at", "updated_at")
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# 順番注意！！Service-Office-Companyの順番Serializerが使えないから
class ServiceSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    officeNumber = serializers.CharField(
        validators=[validators.UniqueValidator(queryset=Service.objects.all(), message='重複！')])

    class Meta:
        model = Service
        fields = ("id", "officeNumber", "serviceType", "capacity", "created_at", "updated_at", "office")


class OfficeSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Office
        fields = ("id", "officeName", "postalCode", "address", "telephoneNumber", "faxNumber", "email", "humanName",
                  "created_at", "updated_at", "service", "company")

class CompanySerializer(serializers.ModelSerializer):
    office = OfficeSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Company
        fields = ("id", "companyName", "companyNumber", "postalCode", "address", "telephoneNumber", "faxNumber",
                  "email", "humanName", "created_at", "updated_at", "office")
