from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import (CustomUser,
                     StudentProfile,
                     UniversitySupervisorProfile,
                     CompanySupervisorProfile,
                     CompanyProfile)

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.account_type=="STUDENT":
            StudentProfile.objects.create(user=instance)

        elif instance.account_type == "UNIVERSITY_SUPERVISOR":
            UniversitySupervisorProfile.objects.create(user=instance)

        elif instance.account_type == "COMPANY":
            CompanyProfile.objects.create(user=instance)

        elif instance.account_type == "COMPANY_SUPERVISOR":
            CompanySupervisorProfile.objects.create(user=instance)