from django.urls import path
from . import views

urlpatterns = [
    
    path('customUser', views.CustomUserListCreateAPIView.as_view(), name='student-list-create'),  #s7
    path('user/<int:pk>/', views.CustomUserDeleteAPIView.as_view(), name='delete_user'),
    path('user/users', views.CustomUserList.as_view(), name='custom-user-list'),#s7
    path('userEmail/<int:pk>/', views.CustomUserGetEmailAPIView.as_view(), name='user_email'),
    path('me',views.RetrieveUserView.as_view()),#s7
    path('register/student', views.RegisterStudentView.as_view()),#s7
    path('register/unisuper', views.RegisterUniSuperView.as_view()),#s7
    path('company/register/compsuper/<int:id>', views.CompanyCompanySuperRegisterView.as_view()),#s7
    path('register/company', views.RegisterCompanyView.as_view()),#s7
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),#s7


    # ********************   STUDENT   ***************
    path('stdprof/<int:pk>',views.RetrieveStudentProfileView.as_view()), #Retrive student profile data
    path('std/stdprof/<int:pk>',views.StdProfileUpdate.as_view()), # Update student profile data
    path('user/studentProfile10/<int:pk>', views.StudentDetail10.as_view(), name='student-detail'),#s7

    #search company profiles :)
    path('company-profiles', views.CompanyProfileFilterView.as_view(), name='company-profile-filter'),
    

    #search std profiles :)
    path('student-profiles', views.StudentProfileFilterView.as_view(), name='student-profile-filter'),
    
    path('user/company', views.CompanyList.as_view(), name='company-list'),#s7
    path('posts/<int:pk>', views.CompPostList.as_view(), name='post_list'),
    path('company/student/trainingApplication', views.TrainingApplicationCreate.as_view(), name='training-application-create'),#s7
    # the company that std applied to
    path('company/student/trainingApplications/<int:pk>', views.TrainingApplicationStudentList.as_view(), name='training-application-create'),#s7
    
    


    # ********************   UNIVERSITY SUPERVISOR   ***************
    path('uniprof/<int:pk>',views.RetrieveUniversitySupervisorProfileView.as_view()),#s7
    path('user/universitysuper/<int:pk>/students', views.UniversitySupervisorStudentList.as_view()),#s7
    #using uinversity supervisor id
    path('unisuper/trainingApplications/<int:pk>', views.TrainingApplicationUniSuperList.as_view(), name='training-application-company'),#s7



    # ********************   COMPANY   ***************
    path('companyprof/<int:pk>',views.RetrieveCompanyProfileView.as_view()),#s7
    path('user/companySupervisors', views.CompanySupervisorList.as_view(), name='company-supervisor-list'),#s7
    path('user/student/assign/companySupervisor/<int:id>', views.AssignCompanySupervisor.as_view()),#s7
    path('user/compsuper/assign/company/<int:id>', views.AssignCompanySuper.as_view()),#s7
    # company list of all students and company supervisors
    path('user/company/<int:pk>/students', views.CompanyStudentList.as_view()),#s7
    path('user/company/<int:pk>/CompSupervisors', views.CompanyCompSuperList.as_view()),#s7
    path('user/companySupervisor/<int:pk>', views.CompanySupervisorDetail.as_view(), name='company-supervisor-detail'),#s7
    
    # Posts
    path('company/posts', views.PostList.as_view(), name='post-list'),#s7
    path('company/post/<int:pk>', views.PostCreateview.as_view(), name='post-create'),#s7
    path('company/post', views.PostCreateview.as_view(), name='post-create'),#s7
    path('company/post/<int:id>/', views.PostUpdateView.as_view(), name='post-update'),#s7
    path('post/<int:pk>', views.PostRetrive.as_view(), name='post_retrive'),

    # using company id
    path('company/company/trainingApplications/<int:pk>', views.TrainingApplicationCompanyList.as_view(), name='training-application-company'),#s7
    

    # ********************   COMPANY SUPERVISOR   ***************
    path('companysuperprof/<int:pk>',views.RetrieveCompanySupervisorProfileView.as_view()),#s7
    path('companysuperprof/get/<int:pk>',views.CompanySupervisorProfileView.as_view()),#s7
    path('user/companysuper/<int:pk>/students', views.CompanySupervisorStudentList.as_view()),#s7
    # report
    # pk is student id
    path('user/reports/<int:pk>', views.WeeklyReportList.as_view(), name='weekly_report_list'),
    path('user/report/<int:pk>', views.WeeklyReportCreate.as_view(), name='weekly_report_create'),
    path('user/report/update/<int:pk>', views.WeeklyReportUpdate.as_view(), name='weekly_report_update'),
    path('weeklyreport/<int:pk>', views.WeeklyReportCreateSign.as_view(), name='weeklyreport_create'),
    
    # ********************   DEPARTMENT   ***************
    path('user/universitySupervisors', views.UniversitySupervisorList.as_view(), name='university-supervisor-list'),#s7
    path('user/studentProfiles', views.StudentList.as_view(), name='student-list'),#s7
    # When Application is accepted by department
    path('user/student/assign/company/<int:id>', views.AssignCompany.as_view()),
    # search department
    path('uni-search', views.UniSuperFilterView.as_view(), name='uni-filter'),
    path('user/student/assign/universitySupervisor/<int:id>', views.AssignUniversitySupervisor.as_view()),#s7
    # get all training applications
    path('dep/student/trainingApplications', views.TrainingApplicationDepList.as_view(), name='training-application-list-dep'),#s7
     #using training application id (we used this for evryone)
    path('company/student/trainingApplication/<int:pk>', views.TrainingApplicationRetrive2.as_view(), name='training-application-view'),#s7
    

    # ********************   Registration   ***************
    path('stdupdate/<int:pk>',views.StudentProfileView.as_view()),#s7
    path('user/universitySupervisorProfile/<int:pk>', views.UniversitySupervisorDetail.as_view(), name='university-supervisor-profile-detail'),#s7
    path('user/studentProfile/<int:pk>', views.StudentDetail.as_view(), name='student-detail'),#s7
    

    # path('user/company/<int:pk>', views.CompanyDetail.as_view(), name='company-detail'),#s7

]