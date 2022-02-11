from rest_framework import serializers
from .models import Company, Office
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# 順番注意！！Office-Companyの順番CompanySerializerが使えないから
class OfficeSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Office
        fields = ("id", "officeName", "postalCode", "address", "telephoneNumber", "faxNumber", "email", "humanName",
                  "capacity", "created_at", "updated_at", "company")


class CompanySerializer(serializers.ModelSerializer):
    office = OfficeSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Company
        fields = ("id", "companyName", "companyNumber", "postalCode", "address", "telephoneNumber", "faxNumber",
                  "email", "humanName", "created_at", "updated_at", "office")


