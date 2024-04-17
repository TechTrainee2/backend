from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import (CustomUser,
                     StudentProfile,
                     UniversitySupervisorProfile,
                     CompanyProfile,
                     CompanySupervisorProfile,
                     )

CustomUser = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password','account_type')

    def validate(self, data):
        user = CustomUser(**data)
        password = data.get('password')

        try:
            validate_password(password, user)
        except exceptions.ValidationError as e:
            serializer_errors = serializers.as_serializer_error(e)
            raise exceptions.ValidationError(
                {'password': serializer_errors['non_field_errors']}
            )

        return data


    def create(self, validated_data):
        user = CustomUser.objects.create_user(
        email=validated_data['email'],
        password=validated_data['password'],
        account_type = validated_data["account_type"]
    )

        return user



class UserGETSerializer(serializers.ModelSerializer):

  class Meta:
    model =CustomUser
    fields = ["id",'email','account_type']
    read_only_fields = ["id"]
        
class StdProfileGETSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False) 
    img_bk = serializers.ImageField(required=False)
    cv = serializers.FileField(required=False)
    user = UserGETSerializer()
    class Meta:
        model =StudentProfile
        fields ="__all__"

class UniSuperGETSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False) 
    img_bk = serializers.ImageField(required=False)
    user = UserGETSerializer()
    class Meta:
        model =UniversitySupervisorProfile
        fields ="__all__"

class CompanyGETSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False) 
    img_bk = serializers.ImageField(required=False)
    user = UserGETSerializer()
    class Meta:
        model =CompanyProfile
        fields ="__all__"

   

class CompanySuperGETSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False) 
    img_bk = serializers.ImageField(required=False)
    user = UserGETSerializer()
    class Meta:
        model =CompanySupervisorProfile
        fields ="__all__"