from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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

# CustomUser = get_user_model()


# class AssignUniversitySupervisorSerializer(serializers.ModelSerializer):
#     email = serializers.CharField(source='user.email')
#     image_url = serializers.SerializerMethodField()
#     class Meta:
#         model = UniversitySupervisor
#         fields = ['email', 'img']
            
#     def get_image_url(self, obj):
#         return 

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['email'] = user.email
        token['password'] = user.password
        # ...
 
        return token
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ['user']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ['user']

class CompanySupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanySupervisor
        fields = '__all__'
        read_only_fields = ['user']


class UniversitySupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversitySupervisor
        fields = '__all__'
        read_only_fields = ['user']

class StudentSerializer(serializers.ModelSerializer):
    # department = DepartmentSerializer()
    # company = CompanySerializer()
    # company_supervisor = CompanySupervisorSerializer()
    # university_supervisor = UniversitySupervisorSerializer()

    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['user']

class RegisterStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        read_only_fields = ["user"]
        fields = '__all__'

class RegisterUniversitySuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversitySupervisor
        read_only_fields = ["user"]
        fields = '__all__'

class CompanyRegisterCompSuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanySupervisor
        read_only_fields = ["user"]
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
        fields = '__all__'