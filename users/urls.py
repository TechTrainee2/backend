from django.urls import path
from . import views

urlpatterns = [
    
    path('customUser', views.CustomUserListCreateAPIView.as_view(), name='student-list-create'),
    path('me',views.RetrieveUserView.as_view()),
    path('stdprof/<int:pk>',views.RetrieveStudentProfileView.as_view()),
    path('uniprof/<int:pk>',views.RetrieveUniSuperProfileView.as_view()),
    path('companyprof/<int:pk>',views.RetrieveCompanyProfileView.as_view()),
    path('companySuperprof/<int:pk>',views.RetrieveCompanySuperProfileView.as_view()),


]