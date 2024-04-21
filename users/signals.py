from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import (
                    Student,
                    StudentProfile, 
                    UniversitySupervisor, 
                    UniversitySupervisorProfile, 
                    Company, 
                    CompanyProfile, 
                    CompanySupervisor, 
                    CompanySupervisorProfile,
                    CustomUser,
                    )


@receiver(post_save, sender=CustomUser)
def create_company_and_profile(sender, instance, created, **kwargs):
    if created and instance.account_type == "COMPANY":
        company, created = Company.objects.get_or_create(user=instance)
        CompanyProfile.objects.get_or_create(company=company)

@receiver(post_save, sender=CustomUser)
def create_companySupervisor_and_profile(sender, instance, created, **kwargs):
    if created and instance.account_type == "COMPANY_SUPERVISOR":
        company_supervisor, created = CompanySupervisor.objects.get_or_create(user=instance)
        CompanySupervisorProfile.objects.get_or_create(company_supervisor=company_supervisor)

@receiver(post_save, sender=CustomUser)
def create_student_and_profile(sender, instance, created, **kwargs):
    if created and instance.account_type == "STUDENT":
        student, created = Student.objects.get_or_create(user=instance)
        StudentProfile.objects.get_or_create(student=student)

@receiver(post_save, sender=CustomUser)
def create_universitySupervisor_and_profile(sender, instance, created, **kwargs):
    if created and instance.account_type == "UNIVERSITY_SUPERVISOR":
        university_supervisor, created = UniversitySupervisor.objects.get_or_create(user=instance)
        UniversitySupervisorProfile.objects.get_or_create(university_supervisor=university_supervisor)