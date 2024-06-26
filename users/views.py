from django.http import Http404
from django.shortcuts import get_object_or_404, render
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
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
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
    WeeklyReport
    )
from .serializers import (
    CompanyRegisterCompSuperSerializer,
    RegisterCompanySerializer,
    RegisterUniversitySuperSerializer,
    StdProfileGETSerializer2,
    StudentSerializer, 
    DepartmentSerializer, 
    CompanySerializer, 
    CompanySupervisorSerializer,
    UniSuperGETSerializer2,
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
    WeeklyReportSerializer,
    CompanySupervisorProfileSerializer2,
    StudentProfileSerializer2,
    UserEmailSerializer,
    UniversitySupervisorSerializer2,
    StudentSerializer3,
    WeeklyReportSerializerCreate,
    CompanyProfileSerializer2,
    

    )

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer3
    permission_classes = [AllowAny]


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]


class StudentDetail10(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer3
    permission_classes = [AllowAny]

class DepartmentList(generics.ListAPIView):
    queryset = Department.objects.all()
    permission_classes = [AllowAny]
    serializer_class = DepartmentSerializer

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]

class CompanySupervisorList(generics.ListAPIView):
    queryset = CompanySupervisor.objects.all()
    serializer_class = CompanySupervisorSerializer
    permission_classes = [AllowAny]

class CompanySupervisorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanySupervisor.objects.all()
    serializer_class = CompanySupervisorSerializer
    permission_classes = [AllowAny]

class UniversitySupervisorList(generics.ListAPIView):
    queryset = UniversitySupervisor.objects.all()
    serializer_class = UniversitySupervisorSerializer2
    permission_classes = [AllowAny]

class UniversitySupervisorStudentList(generics.ListAPIView):
    serializer_class = StudentProfileSerializer2
    permission_classes = [AllowAny]

    def get_queryset(self):
        supervisor_id = self.kwargs['pk']
        supervisor = UniversitySupervisor.objects.get(user_id=supervisor_id)
        student = Student.objects.filter(university_supervisor=supervisor)
        # @TODO: Add company supervisor profile for each compant supervisor and return it as a query
        student_profiles = StudentProfile.objects.filter(student__in=student)
        return student_profiles
    
class CompanySupervisorStudentList(generics.ListAPIView):
    serializer_class = StudentProfileSerializer2
    permission_classes = [AllowAny]
    def get_queryset(self):
        supervisor_id = self.kwargs['pk']
        supervisor = CompanySupervisor.objects.get(user_id=supervisor_id)
        student = Student.objects.filter(company_supervisor=supervisor)
        student_profiles = StudentProfile.objects.filter(student__in=student)
        return student_profiles   
    
    
class CompanyCompSupervisorList(generics.ListAPIView):
    serializer_class = CompanySupervisorSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        comp_id = self.kwargs['pk']
        companyAcc = Company.objects.get(user_id=comp_id)
        return CompanySupervisor.objects.filter(company=companyAcc)
    
class CompanyStudentList(generics.ListAPIView):
    serializer_class = StudentProfileSerializer2
    permission_classes = [AllowAny]
    def get_queryset(self):
        company_id = self.kwargs['pk']
        companyAcc = Company.objects.get(user_id=company_id)
        student = Student.objects.filter(company=companyAcc)
        student_profiles = StudentProfile.objects.filter(student__in=student)
        return student_profiles   
    
class CompanyCompSuperList(generics.ListAPIView):
    
    serializer_class = CompanySupervisorProfileSerializer2
    permission_classes = [AllowAny]
    def get_queryset(self):
        company_id = self.kwargs['pk']
        companyAcc = Company.objects.get(user_id=company_id)
        company_supervisors = CompanySupervisor.objects.filter(company=companyAcc)
        company_supervisor_profiles = CompanySupervisorProfile.objects.filter(company_supervisor__in=company_supervisors)
        return company_supervisor_profiles
          

class AssignUniversitySupervisor(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [AllowAny]

    def patch(self, request, *args, **kwargs):
        student = self.get_object()
        supervisor_id = request.data.get('university_supervisor')

        if supervisor_id is not None:
            try:
                university_supervisor = UniversitySupervisor.objects.get(user_id=supervisor_id)
            except UniversitySupervisor.DoesNotExist:
                return Response({"error": f"university_supervisor with id {supervisor_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            student.university_supervisor = university_supervisor
        else:
            student.university_supervisor = None
            
        student.save()
        return Response(StudentSerializer(student).data)

class AssignCompanySupervisor(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [AllowAny]

    def patch(self, request, *args, **kwargs):
        student = self.get_object()
        supervisor_id = request.data.get('company_supervisor')

        if supervisor_id is not None:
            try:
                company_supervisor = CompanySupervisor.objects.get(user_id=supervisor_id)
            except CompanySupervisor.DoesNotExist:
                return Response({"error": f"company_supervisor with id {supervisor_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            student.company_supervisor = company_supervisor
        else:
            student.company_supervisor = None
            
        student.save()
        return Response(StudentSerializer(student).data)

class AssignCompany(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [AllowAny]

    def patch(self, request, *args, **kwargs):
        student = self.get_object()
        company_id = request.data.get('company')

        if company_id is not None:
            try:
                company = Company.objects.get(user_id=company_id)
            except Company.DoesNotExist:
                return Response({"error": f"Company with id {company_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            student.company = company
        else:
            student.company = None

        student.save()
        return Response(StudentSerializer(student).data)

#for testing 
class AssignCompanySuper(generics.UpdateAPIView):
    queryset = CompanySupervisor.objects.all()
    serializer_class = CompanySupervisorSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [AllowAny]

    def patch(self, request, *args, **kwargs):
        companysuper = self.get_object()
        company_id = request.data.get('company')

        if company_id is not None:
            try:
                company = Company.objects.get(user_id=company_id)
            except Company.DoesNotExist:
                return Response({"error": f"Company with id {company_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            companysuper.company = company
        else:
            companysuper.company = None

        companysuper.save()
        return Response(CompanySupervisorSerializer(companysuper).data)

class UniversitySupervisorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UniversitySupervisor.objects.all()
    serializer_class = UniversitySupervisorSerializer
    permission_classes = [AllowAny]

class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    

class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]


class CustomUserListCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class CustomUserDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class CustomUserGetEmailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserEmailSerializer
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

    def get(self, request):
         user = request.user
         user = UserGETSerializer(user)

         return Response(user.data, status=status.HTTP_200_OK)
    
class RegisterStudentView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterStudentSerializer
    permission_classes = [AllowAny]        #@TODO: Change to IsAuthenticated

    def post(self, request):
        data = request.data
        user = CustomUser.objects.create_user(email=data["email"], password=data["password"],account_type=data["account_type"])
        
        user.account_type = 'STUDENT'
        user.save()
    

        student, created = Student.objects.get_or_create(user=user)
        student.first_name = data["first_name"]
        student.last_name = data["last_name"]
        student.save()


        return Response(StudentSerializer(student).data, status=status.HTTP_200_OK)
        

class RegisterUniSuperView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterUniversitySuperSerializer
    permission_classes = [AllowAny]        #@TODO: Change to IsAuthenticated

    def post(self, request):
        data = request.data
        user = CustomUser.objects.create_user(email=data["email"], password=data["password"],account_type=data["account_type"])
        
        user.account_type = 'UNIVERSITY_SUPERVISOR'
        user.save()
    

        uni_super, created = UniversitySupervisor.objects.get_or_create(user=user)
        uni_super.first_name = data["first_name"]
        uni_super.last_name = data["last_name"]
        uni_super.save()


        return Response(UniversitySupervisorSerializer(uni_super).data, status=status.HTTP_200_OK)


class RegisterCompanyView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterCompanySerializer
    permission_classes = [AllowAny]        #@TODO: Change to IsAuthenticated

    def post(self, request):
        data = request.data
        user = CustomUser.objects.create_user(email=data["email"], password=data["password"],account_type=data["account_type"])
        
        user.account_type = 'COMPANY'
        user.save()
    

        company, created = Company.objects.get_or_create(user=user)
        company.name = data["name"]
        company.comp_id = data["comp_id"]
        
        company.save()


        return Response(CompanySerializer(company).data, status=status.HTTP_200_OK)


class CompanyCompanySuperRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CompanyRegisterCompSuperSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [AllowAny]        #@TODO: Change to IsAuthenticated

    def post(self, request, id=None):
        data = request.data
        user = CustomUser.objects.create_user(email=data["email"], password=data["password"],account_type=data["account_type"])

        companysupervisor, created = CompanySupervisor.objects.get_or_create(user=user)
        companysupervisor.first_name = data["first_name"]
        companysupervisor.last_name = data["last_name"]
        companysupervisor.role=data["role"]
        user.account_type = 'COMPANY_SUPERVISOR'
        user.save()
        
        company = Company.objects.get(user_id=id)  
        companysupervisor.company = company
        
        companysupervisor.save()
        return Response({"message": "Company supervisor created successfully"}, status=status.HTTP_201_CREATED)

class RetrieveStudentProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StdProfileGETSerializer
    permission_classes = [AllowAny]

class StudentProfileFilterView(generics.ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StdProfileGETSerializer2
    filter_backends = [filters.SearchFilter]
    search_fields = ['student__first_name', 'student__last_name']
    permission_classes = [AllowAny] 

class CompanyProfileFilterView(generics.ListAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer2
    filter_backends = [filters.SearchFilter]
    search_fields = ['company__name']
    permission_classes = [AllowAny]


class UniSuperFilterView(generics.ListAPIView):
    queryset = UniversitySupervisorProfile.objects.all()
    serializer_class = UniSuperGETSerializer2
    filter_backends = [filters.SearchFilter]
    search_fields = ['university_supervisor__first_name', 'university_supervisor__last_name']
    permission_classes = [AllowAny]

class StdProfileUpdate(generics.UpdateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StdProfileGETSerializer
    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
        student_id = kwargs.get('pk')  # Get student_id from URL parameters

        try:
            student = Student.objects.get(pk=student_id)
            student_profile = StudentProfile.objects.get(student=student)
        except Student.DoesNotExist:
            return Response({"error": f"Student with id {student_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except StudentProfile.DoesNotExist:
            return Response({"error": f"StudentProfile for student with id {student_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        cv_file = request.FILES.get('cv', None)

        serializer = self.get_serializer(student_profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(cv=cv_file)

        return Response(serializer.data)

class StudentProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

class RetrieveUniversitySupervisorProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UniversitySupervisorProfile.objects.all()
    serializer_class =UniSuperGETSerializer
    permission_classes = [AllowAny]

class RetrieveCompanyProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class =CompanyGETSerializer
    permission_classes = [AllowAny]

class RetrieveCompanySupervisorProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanySupervisorProfile.objects.all()
    serializer_class =CompanySuperGETSerializer
    permission_classes = [AllowAny]

class CompanySupervisorProfileView(generics.RetrieveAPIView):
    queryset = CompanySupervisorProfile.objects.all()
    serializer_class =CompanySupervisorProfileSerializer2
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
    
class CompPostList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        company_id = self.kwargs['pk']
        company = get_object_or_404(Company, user_id=company_id)
        return Post.objects.filter(company=company)
    
class PostRetrive(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    queryset = Post.objects.all()


class PostCreateview(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

class PostUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [AllowAny]

class TrainingApplicationCreate(generics.CreateAPIView):
    queryset = TrainingApplication.objects.all()
    serializer_class = TrainingApplicationSerializer
    permission_classes = [AllowAny]

class TrainingApplicationDepList(generics.ListAPIView):
    queryset = TrainingApplication.objects.all()
    serializer_class = TrainingApplicationSerializer
    permission_classes = [AllowAny]

class TrainingApplicationRetrive(generics.RetrieveAPIView):
    queryset = TrainingApplication.objects.all()
    serializer_class = TrainingApplicationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        student_id = self.kwargs['pk']
        student = get_object_or_404(Student, user_id=student_id)
        return TrainingApplication.objects.filter(student=student)
        
class TrainingApplicationRetrive2(generics.RetrieveUpdateAPIView):
    serializer_class = TrainingApplicationSerializer
    permission_classes = [AllowAny]
    queryset = TrainingApplication.objects.all()

class TrainingApplicationStudentList(generics.ListAPIView):
    serializer_class = TrainingApplicationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        student_id = self.kwargs['pk']
        student = get_object_or_404(Student, user_id=student_id)
        return TrainingApplication.objects.filter(student=student)
    
class TrainingApplicationCompanyList(generics.ListAPIView):
    serializer_class = TrainingApplicationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        company_id = self.kwargs['pk']
        company = get_object_or_404(Company, user_id=company_id)
        return TrainingApplication.objects.filter(company=company)

class TrainingApplicationUniSuperList(generics.ListAPIView):
    serializer_class = TrainingApplicationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        unisuper_id = self.kwargs['pk']
        unisuper = get_object_or_404(UniversitySupervisor, user_id=unisuper_id)
        return TrainingApplication.objects.filter(university_supervisor=unisuper)

class TrainingApplicationStatus(generics.RetrieveUpdateAPIView):
    queryset = TrainingApplication.objects.all()
    serializer_class = TrainingApplicationSerializer
    permission_classes = [AllowAny]


class WeeklyReportList(generics.ListAPIView):
    serializer_class = WeeklyReportSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        student_id = self.kwargs['pk']
        return WeeklyReport.objects.filter(student=student_id)


class WeeklyReportCreate(generics.CreateAPIView):
    queryset = WeeklyReport.objects.all()
    serializer_class = WeeklyReportSerializerCreate
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        student_id = kwargs.get('pk')  # Get student_id from URL parameters

        try:
            student = Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            return Response({"error": f"Student with id {student_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(student=student)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
   
    

class WeeklyReportCreateSign(generics.CreateAPIView):
    queryset = WeeklyReport.objects.all()
    serializer_class = WeeklyReportSerializerCreate
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        student_id = kwargs.get('pk')  # Get student_id from URL parameters

        try:
            student = Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            return Response({"error": f"Student with id {student_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        companySupervisorSignature_file = request.FILES.get('companySupervisorSignature', None)
        universitySupervisorSignature_file = request.FILES.get('universitySupervisorSignature', None)

        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(student=student, universitySupervisorSignature=universitySupervisorSignature_file, companySupervisorSignature=companySupervisorSignature_file)

        return Response(serializer.data)



class WeeklyReportUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeeklyReport.objects.all()
    serializer_class = WeeklyReportSerializer
    permission_classes = [AllowAny]
