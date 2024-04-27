from django.contrib import admin
from .models import CustomUser, Department, DepartmentAdminModel, UniversitySupervisor, UniversitySupervisorProfile, Student, StudentProfile, WeeklyReport, Company, CompanyProfile, Post, CompanySupervisor, CompanySupervisorProfile

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'account_type', 'is_active', 'is_staff']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class DepartmentAdminAdmin(admin.ModelAdmin):
    list_display = ['user', 'department']

class UniversitySupervisorAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'phone', 'location', 'department']

class UniversitySupervisorProfileAdmin(admin.ModelAdmin):
    list_display = ['university_supervisor', 'img', 'img_bk']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'department']

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['student', 'img', 'img_bk', 'bio', 'cv','phone', 'location']

class WeeklyReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'universitySupervisorSignature','companySupervisorSignature', 'company_supervisor', 'student', 'week_number', 'date', 'report_details']

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'phone', 'location', 'comp_id']

class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['company', 'img', 'img_bk', 'bio']

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'title', 'training_mode', 'post_details']

class CompanySupervisorAdmin(admin.ModelAdmin):
    list_display = ['user', 'company', 'first_name', 'last_name', 'phone', 'location', 'role']

class CompanySupervisorProfileAdmin(admin.ModelAdmin):
    list_display = ['company_supervisor', 'img', 'img_bk']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(DepartmentAdminModel, DepartmentAdminAdmin)
admin.site.register(UniversitySupervisor, UniversitySupervisorAdmin)
admin.site.register(UniversitySupervisorProfile, UniversitySupervisorProfileAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(WeeklyReport, WeeklyReportAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyProfile, CompanyProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(CompanySupervisor, CompanySupervisorAdmin)
admin.site.register(CompanySupervisorProfile, CompanySupervisorProfileAdmin)
