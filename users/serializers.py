from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import (CustomUser,
                    StudentProfile,
                    UniversitySupervisorProfile,
                    CompanyProfile,
                    CompanySupervisorProfile,
                    Student,
                    Department,
                    Company,
                    CompanySupervisor,
                    UniversitySupervisor,
                    Post,
                    TrainingApplication,
                     )

CustomUser = get_user_model()




class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    class Meta:
        model = Department
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    class Meta:
        model = Company
        fields = '__all__'

class CompanySupervisorSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    class Meta:
        model = CompanySupervisor
        fields = '__all__'

class UniversitySupervisorSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    department = DepartmentSerializer()
    class Meta:
        model = UniversitySupervisor
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    department = DepartmentSerializer()
    company = CompanySerializer()
    company_supervisor = CompanySupervisorSerializer()
    university_supervisor = UniversitySupervisorSerializer()

    class Meta:
        model = Student
        fields = '__all__'

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
    
    class Meta:
        model =StudentProfile
        fields ="__all__"

class UniSuperGETSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False) 
    img_bk = serializers.ImageField(required=False)
    class Meta:
        model =UniversitySupervisorProfile
        fields ="__all__"

class CompanyGETSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False) 
    img_bk = serializers.ImageField(required=False)
    class Meta:
        model =CompanyProfile
        fields ="__all__"

   

class CompanySuperGETSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False) 
    img_bk = serializers.ImageField(required=False)
    class Meta:
        model =CompanySupervisorProfile
        fields ="__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class TrainingApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingApplication
        fields = ['id', 'student', 'training']