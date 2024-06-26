from django.contrib import admin
from .models import CustomUser, Department, DepartmentAdminModel, UniversitySupervisor, UniversitySupervisorProfile, Student, StudentProfile, WeeklyReport, Company, CompanyProfile, Post, CompanySupervisor, CompanySupervisorProfile, TrainingApplication

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'account_type', 'is_active', 'is_staff']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class DepartmentAdminAdmin(admin.ModelAdmin):
    list_display = ['user', 'department']

class UniversitySupervisorAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'department']

class UniversitySupervisorProfileAdmin(admin.ModelAdmin):
    list_display = ['university_supervisor', 'img', 'img_bk','phone', 'location']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'department']

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['student', 'img', 'img_bk', 'bio', 'cv','phone', 'location']

class WeeklyReportAdmin(admin.ModelAdmin):
    list_display = ['id','date_begin','date_end', 'universitySupervisorSignature','companySupervisorSignature', 'company_supervisor', 'student', 'week_number', 'table_data']

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'comp_id']

class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['company', 'img', 'img_bk', 'bio','phone', 'location']

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'title', 'training_mode', 'post_details']

class CompanySupervisorAdmin(admin.ModelAdmin):
    list_display = ['user', 'company', 'first_name', 'last_name','role']

class CompanySupervisorProfileAdmin(admin.ModelAdmin):
    list_display = ['company_supervisor', 'img', 'img_bk','phone', 'location']

class TrainingApplicationAdmin(admin.ModelAdmin):
    list_display = ['student', 'company','department','university_supervisor','post','department_status','university_supervisor_status','company_status']

# class RegisterAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name']

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
admin.site.register(TrainingApplication, TrainingApplicationAdmin)