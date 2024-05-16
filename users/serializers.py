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
                    WeeklyReport,
                     )

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        token['email'] = user.email
        token['password'] = user.password
 
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
        fields = ['name','comp_id']
        read_only_fields = ['user']

class CompanySupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanySupervisor
        fields = ['first_name',"last_name",'role']
        read_only_fields = ['user']


class UniversitySupervisorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    class Meta:
        model = UniversitySupervisor
        fields = ["first_name","last_name"]
        read_only_fields = ['user']

class UniversitySupervisorSerializer2(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    class Meta:
        model = UniversitySupervisor
        fields = ["first_name","last_name",'user']

class STDprofSupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversitySupervisor
        fields = ['first_name',"last_name"]

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ["first_name","last_name"]
        read_only_fields = ['user','university_supervisor']

# class StudentSerializer10(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ["first_name","last_name","university_supervisor","user"]

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
        
class RegisterCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
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

class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email','account_type')

       

class UserGETSerializer(serializers.ModelSerializer):

  class Meta:
    model =CustomUser
    fields = ["id",'email','account_type']
    read_only_fields = ["id"]
        
class StdProfileGETSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False) 
    img_bk = serializers.ImageField(required=False)
    cv = serializers.FileField(required=False)
    bio=serializers.CharField(required=False)
    phone=serializers.CharField(required=False)
    location=serializers.CharField(required=False)
    student=StudentSerializer()
    
    class Meta:
        model =StudentProfile
        fields =['student','img','img_bk','bio','cv','phone','location']

class UniSuperGETSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False) 
    img_bk = serializers.ImageField(required=False)
    phone=serializers.CharField(required=False)
    location=serializers.CharField(required=False)
    university_supervisor=UniversitySupervisorSerializer()
    class Meta:
        model =UniversitySupervisorProfile
        fields =['university_supervisor','img','img_bk','phone','location']

class UniSuperGETSerializer2(serializers.ModelSerializer):
    img = serializers.ImageField(required=False) 
    img_bk = serializers.ImageField(required=False)
    phone=serializers.CharField(required=False)
    location=serializers.CharField(required=False)
    university_supervisor=UniversitySupervisorSerializer2()
    class Meta:
        model =UniversitySupervisorProfile
        fields =['university_supervisor','img','img_bk','phone','location']

class CompanyGETSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False) 
    img_bk = serializers.ImageField(required=False)
    bio=serializers.CharField(required=False)
    phone=serializers.CharField(required=False)
    location=serializers.CharField(required=False)
    company=CompanySerializer()
    class Meta:
        model =CompanyProfile
        fields =['company','img','img_bk','phone','location','bio']
   

class CompanySuperGETSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False) 
    img_bk = serializers.ImageField(required=False)
    phone=serializers.CharField(required=False)
    location=serializers.CharField(required=False)
    company_supervisor=CompanySupervisorSerializer()
    class Meta:
        model =CompanySupervisorProfile
        fields =['company_supervisor','img','img_bk','phone','location']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class TrainingApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingApplication
        fields = '__all__'

class WeeklyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyReport
        fields = '__all__'
        
class WeeklyReportSerializerCreate(serializers.ModelSerializer):
    universitySupervisorSignature = serializers.FileField(required=False)
    companySupervisorSignature = serializers.FileField(required=False)
    class Meta:
        model = WeeklyReport
        fields = ['report_details', 'week_number', 'date_begin','date_end', 'universitySupervisorSignature', 'companySupervisorSignature', 'table_data']
        read_only_fields = ['student']


class CompanySupervisorSerializer2(serializers.ModelSerializer):
    class Meta:
        model = CompanySupervisor
        fields = ['first_name',"last_name",'user']

class CompanySupervisorProfileSerializer2(serializers.ModelSerializer):
    img = serializers.ImageField(required=False) 
    img_bk = serializers.ImageField(required=False)
    phone=serializers.CharField(required=False)
    location=serializers.CharField(required=False)
    company_supervisor=CompanySupervisorSerializer2()
    class Meta:
        model =CompanySupervisorProfile
        fields =['company_supervisor','img','img_bk','phone','location']

class CompanySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name','comp_id','user']


class StudentSerializer2(serializers.ModelSerializer):
    company_supervisor = CompanySupervisorSerializer2()
    company=CompanySerializer2()
    class Meta:
        model = Student
        fields = ['first_name',"last_name",'user','company_supervisor','company']

class StudentSerializer3(serializers.ModelSerializer):
    company_supervisor = CompanySupervisorSerializer2()
    company=CompanySerializer2()
    university_supervisor=UniversitySupervisorSerializer2()
    class Meta:
        model = Student
        fields = ['first_name',"last_name",'user','company_supervisor','company','university_supervisor']


class StudentProfileSerializer2(serializers.ModelSerializer):
    img = serializers.ImageField(required=False) 
    img_bk = serializers.ImageField(required=False)
    phone=serializers.CharField(required=False)
    location=serializers.CharField(required=False)

    student=StudentSerializer2()
    class Meta:
        model =StudentProfile
        fields =['student','img','img_bk','phone','location']

class CompanyProfileSerializer2(serializers.ModelSerializer):
    img = serializers.ImageField(required=False) 
    img_bk = serializers.ImageField(required=False)
    bio=serializers.CharField(required=False)
    phone=serializers.CharField(required=False)
    location=serializers.CharField(required=False)
    company=CompanySerializer2()
    class Meta:
        model =CompanyProfile
        fields =['company','img','img_bk','phone','location','bio']


# class PostSerializer2(serializers.ModelSerializer):
#     company = CompanySerializer2()
#     class Meta:
#         model = Post
#         fields = ['company','date','post_details','title','training_mode']

class TrainingApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingApplication
        fields = '__all__'


class StdProfileGETSerializer2(serializers.ModelSerializer):
    img = serializers.ImageField(required=False) 
    img_bk = serializers.ImageField(required=False)
    cv = serializers.FileField(required=False)
    bio=serializers.CharField(required=False)
    phone=serializers.CharField(required=False)
    location=serializers.CharField(required=False)
    student=StudentSerializer3()

    
    class Meta:
        model =StudentProfile
        fields =['student','img','img_bk','bio','cv','phone','location']




