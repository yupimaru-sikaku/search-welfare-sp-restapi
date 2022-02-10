from rest_framework.serializers import SerializerMethodField
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

class CompanyDetailSerializer(serializers.ModelSerializer):
    ofiices = SerializerMethodField() #このフィールドを加えると下記のように出力する値を操作できます。
    class Meta:
        model = Company
        fields = ("id", "companyName", "companyNumber", "postalCode", "address", "telephoneNumber", "faxNumber",
                  "email", "humanName", "created_at", "offices")

    def get_offices(self, obj):
        try:
            office_abstruct_contents = OfficeChildSerializer(Office.objects.all().filter(target_office = Company.objects.get(id=obj.id)), many=True).data
            #↑ここを"Comment.objects.all().filter(target_article = Article.objects.get(id=obj.id)"
            #とだけにすると、"Item is not JSON serializable"というエラーが出ますので
            #Serializer(出力させたいもの).data　という処理が必要です。
            return office_abstruct_contents
        except:
            office_abstruct_contents = None
            return office_abstruct_contents

# class CompanySerializer(serializers.ModelSerializer):
#
#     created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
#
#     class Meta:
#         model = Company
#         fields = ("id", "companyName", "companyNumber", "postalCode", "address", "telephoneNumber", "faxNumber",
#                   "email", "humanName", "created_at")

class OfficeSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Office
        fields = ("id", "officeName", "postalCode", "address", "telephoneNumber", "faxNumber", "email", "humanName",
                  "capacity", "created_at")

class OfficeChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ("id", "officeName", "postalCode", "address", "telephoneNumber", "faxNumber", "email", "humanName",
                  "capacity", "created_at", "target_company")