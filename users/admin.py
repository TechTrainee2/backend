from django.contrib import admin

# Register your models here.

# Register your models here.
from django.contrib import admin
from .models import (StudentProfile,
                     UniversitySupervisorProfile,
                     CompanyProfile,
                     CompanySupervisorProfile,
                     )
# from .models import Company
from .models import CustomUser



class CustomUserUsertAdmin(admin.ModelAdmin):
    list_display =["email","account_type"]
    
admin.site.register(CustomUser, CustomUserUsertAdmin)



class StudentProfileUsertAdmin(admin.ModelAdmin):
    list_display =["location","department","phone","cv","img","img_bk"]
    
admin.site.register(StudentProfile, StudentProfileUsertAdmin)


class UniSuperProfileUsertAdmin(admin.ModelAdmin):
    list_display =["location","department","phone","img","img_bk"]
    
admin.site.register(UniversitySupervisorProfile, UniSuperProfileUsertAdmin)


class CompanyProfileUsertAdmin(admin.ModelAdmin):
    list_display =["location","phone","img","img_bk"]
    
admin.site.register(CompanyProfile, CompanyProfileUsertAdmin)


class CompanySuperProfileUsertAdmin(admin.ModelAdmin):
    list_display =["location","role","phone","img","img_bk"]
    
admin.site.register(CompanySupervisorProfile, CompanySuperProfileUsertAdmin)


