from django.http import Http404
from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions,status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

from rest_framework import generics
from .models import (
    UniversitySupervisorProfile,
    Student, 
    Department, 
    Company, 
    CompanySupervisor, 
    UniversitySupervisor, 
    CustomUser,
    StudentProfile,
    CompanyProfile,
    CompanySupervisorProfile,
    Post,
    TrainingApplication,
    )
from .serializers import (
    StudentSerializer, 
    DepartmentSerializer, 
    CompanySerializer, 
    CompanySupervisorSerializer, 
    UniversitySupervisorSerializer, 
    CustomUserSerializer,
    UserSerializer,
    UserGETSerializer,
    StdProfileGETSerializer,
    UniSuperGETSerializer,
    CompanyGETSerializer,
    CompanySuperGETSerializer,
    PostSerializer,
    TrainingApplicationSerializer,
    MyTokenObtainPairSerializer,
    RegisterStudentSerializer,
    )

# class UniversitySupervisorProfileList(generics.ListAPIView):
#     queryset = UniversitySupervisorProfile.objects.all()
#     serializer_class = UniversitySupervisorSerializer

# class UniversitySupervisorProfileDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UniversitySupervisorProfile.objects.all()
#     serializer_class = UniversitySupervisorSerializer

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DepartmentList(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanySupervisorList(generics.ListAPIView):
    queryset = CompanySupervisor.objects.all()
    serializer_class = CompanySupervisorSerializer

class CompanySupervisorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanySupervisor.objects.all()
    serializer_class = CompanySupervisorSerializer

class UniversitySupervisorList(generics.ListAPIView):
    queryset = UniversitySupervisor.objects.all()
    serializer_class = UniversitySupervisorSerializer

class UniversitySupervisorStudentList(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        supervisor_id = self.kwargs['pk']
        supervisor = UniversitySupervisor.objects.get(user_id=supervisor_id)
        return Student.objects.filter(university_supervisor=supervisor)

class UniversitySupervisorStudentList(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        supervisor_id = self.kwargs['pk']
        supervisor = UniversitySupervisor.objects.get(user_id=supervisor_id)
        return Student.objects.filter(university_supervisor=supervisor)

class AssignUniversitySupervisor(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [AllowAny]

    def patch(self, request, *args, **kwargs):
        student = self.get_object()
        supervisor_id = request.data.get('university_supervisor')
        supervisor = UniversitySupervisor.objects.get(user_id=supervisor_id)
        student.university_supervisor = supervisor
        student.save()
        return Response(StudentSerializer(student).data)
    
class UniversitySupervisorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UniversitySupervisor.objects.all()
    serializer_class = UniversitySupervisorSerializer

class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer



class CustomUserListCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class LoginView(generics.GenericAPIView):
    pass

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            response.set_cookie('access', response.data['access'])  # Set JWT token as a cookie
        return response

class RetrieveUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserGETSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get(self, request):
    #     user = request.user
    #     user = UserGETSerializer(user)

    #     return Response(user.data, status=status.HTTP_200_OK)
    
class RegisterStudentView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterStudentSerializer
    permission_classes = [AllowAny]        #@TODO: Change to IsAuthenticated
    def post(self, request):
        user = request.data.get['email']
        serializer = RegisterStudentSerializer(data=user)
        user.account_type = 'STUDENT'
        user.save()

class RegisterUniSuperView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]        #@TODO: Change to IsAuthenticated
    def perform_create(self, serializer):
        user = serializer.save()
        user.account_type = 'UNIVERSITY_SUPERVISOR'
        user.save()

class CompanyCompanySuperRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]        #@TODO: Change to IsAuthenticated
    def perform_create(self, serializer):
        user = serializer.save()
        user.account_type = 'COMPANY_SUPERVISOR'
        user.save()

class RetrieveStudentProfileView(generics.RetrieveAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StdProfileGETSerializer
    permission_classes = [AllowAny]


class RetrieveUniversitySupervisorProfileView(generics.RetrieveAPIView):
    queryset = UniversitySupervisorProfile.objects.all()
    serializer_class =UniSuperGETSerializer
    permission_classes = [AllowAny]

class RetrieveCompanyProfileView(generics.RetrieveAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class =CompanyGETSerializer
    permission_classes = [AllowAny]

class RetrieveCompanySupervisorProfileView(generics.RetrieveAPIView):
    queryset = CompanySupervisorProfile.objects.all()
    serializer_class =CompanySuperGETSerializer
    permission_classes = [AllowAny]

@method_decorator(csrf_exempt, name='dispatch')
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-date')  # Order by date in descending order
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        title = self.request.query_params.get('title')
        company = self.request.query_params.get('company')
        training_mode = self.request.query_params.get('training_mode')

        queryset = super().get_queryset()

        if title:
            queryset = queryset.filter(title=title)
        if company:
            queryset = queryset.filter(company=company)
        if training_mode:
            queryset = queryset.filter(training_mode=training_mode)

        return queryset

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

class PostUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [AllowAny]

class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [AllowAny]

class TrainingApplicationCreate(generics.CreateAPIView):
    queryset = TrainingApplication.objects.all()
    serializer_class = TrainingApplicationSerializer

class TrainingApplicationUpdate(generics.UpdateAPIView):
    queryset = TrainingApplication.objects.all()
    serializer_class = TrainingApplicationSerializer

