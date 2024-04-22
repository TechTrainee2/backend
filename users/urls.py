from django.urls import path
from . import views

urlpatterns = [
    
    path('customUser', views.CustomUserListCreateAPIView.as_view(), name='student-list-create'),  #s7
    path('me',views.RetrieveUserView.as_view()),#s7
    path('register/student', views.RegisterStudentView.as_view()),
    path('register/unisuper', views.RegisterUniSuperView.as_view()),
    path('company/register/compsuper', views.CompanyCompanySuperRegisterView.as_view()),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('stdprof/<int:pk>',views.RetrieveStudentProfileView.as_view()),#s7
    path('uniprof/<int:pk>',views.RetrieveUniversitySupervisorProfileView.as_view()),#s7
    path('companyprof/<int:pk>',views.RetrieveCompanyProfileView.as_view()),#s7
    path('companysuperprof/<int:pk>',views.RetrieveCompanySupervisorProfileView.as_view()),#s7
    
    path('user/universitySupervisors', views.UniversitySupervisorList.as_view(), name='university-supervisor-list'),
    path('user/companySupervisors', views.CompanySupervisorList.as_view(), name='company-supervisor-list'),
    path('user/company', views.CompanyList.as_view(), name='company-list'),
    path('user/studentProfiles', views.StudentList.as_view(), name='student-list'),
    path('user/departments', views.DepartmentList.as_view(), name='department-list'),
    path('user/users', views.CustomUserList.as_view(), name='custom-user-list'),

    # path('user/student/assign/universitySupervisor/<int:id>', views.AssignUniversitySupervisor.as_view()),
    path('user/university/<int:pk>/students', views.UniversitySupervisorStudentList.as_view()),

    path('user/universitySupervisorProfile/<int:pk>', views.UniversitySupervisorDetail.as_view(), name='university-supervisor-profile-detail'),
    path('user/studentProfile/<int:pk>', views.StudentDetail.as_view(), name='student-detail'),
    path('user/company/<int:pk>', views.CompanyDetail.as_view(), name='company-detail'),
    path('user/companySupervisor/<int:pk>', views.CompanySupervisorDetail.as_view(), name='company-supervisor-detail'),
    path('user/universitySupervisor/<int:pk>', views.UniversitySupervisorDetail.as_view(), name='university-supervisor-detail'),
    path('user/user/<int:pk>', views.CustomUserDetail.as_view(), name='custom-user-detail'),

    path('company/posts', views.PostList.as_view(), name='post-list'),
    path('company/post/<int:pk>', views.PostDetail.as_view(), name='post-detail'),
    path('company/post/<int:id>/', views.PostUpdateView.as_view(), name='post-update'),
    path('company/post/<int:id>/', views.PostDeleteView.as_view(), name='post-delete'),


    path('company/trainingApplication', views.TrainingApplicationCreate.as_view(), name='training-application-create'),
    path('company/trainingApplication/<int:pk>', views.TrainingApplicationUpdate.as_view(), name='training-application-update'),


]