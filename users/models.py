from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin,AbstractBaseUser
from django.contrib.auth.models import User

from django.contrib.postgres.fields import JSONField

class UserAccountManager(BaseUserManager):
  def create_user(self, email,password=None,**other_fields):
    if not email:
      raise ValueError('Users must have an email address')

    email = self.normalize_email(email)
    email = email.lower()

    user = self.model(
 
      email=email,
    #   account_type= self.account_type,
      **other_fields
    )

    user.set_password(password)
    user.save(using=self._db)

    return user
  
  def create_superuser(self, email, password=None ,**other_fields):
    user = self.create_user(
      email,
      password=password,
      **other_fields
    )

    user.is_staff = True
    user.is_superuser = True
    user.account_type="ADMIN"
    user.save(using=self._db)

    return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ACCOUNT_TYPE_CHOICES = (
        ('STUDENT', 'Student'),
        ('UNIVERSITY_SUPERVISOR', 'University Supervisor'),
        ('COMPANY', 'Company'),
        ('COMPANY_SUPERVISOR', 'Company Supervisor'),
        ('DEPARTMENT', 'Department'),
        ('REGISTRATION', 'Registration'),
        ("ADMIN","Admin"),
    )
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPE_CHOICES, default="ADMIN")
  
    email = models.EmailField(unique=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email





class Department(models.Model):
    name = models.CharField(max_length=50)

class DepartmentAdminModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class UniversitySupervisor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True, blank=True)

class UniversitySupervisorProfile(models.Model):
    university_supervisor = models.OneToOneField(UniversitySupervisor, on_delete=models.CASCADE,primary_key=True)
    img = models.ImageField(upload_to="files\\images", null=True, blank=True)
    img_bk = models.ImageField(upload_to="files\\images", null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True, blank=True)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)
    company_supervisor = models.ForeignKey('CompanySupervisor', on_delete=models.SET_NULL, null=True, blank=True)
    university_supervisor = models.ForeignKey(UniversitySupervisor, on_delete=models.SET_NULL, null=True, blank=True)

class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE,primary_key=True)
    img = models.ImageField(upload_to="files\\images", null=True, blank=True)
    img_bk = models.ImageField(upload_to="files\\images", null=True, blank=True)
    bio = models.CharField(max_length=50, null=True, blank=True)
    cv = models.FileField(upload_to="files\\cvs", null=True, blank=True)
    phone = models.CharField(max_length=50,null=True, blank=True)
    location = models.CharField(max_length=50,null=True, blank=True)
    
class WeeklyReport(models.Model):
    universitySupervisorSignature = models.FileField(upload_to="files\\signatures", null=True, blank=True)
    companySupervisorSignature = models.FileField(upload_to="files\\signatures", null=True, blank=True)
    company_supervisor = models.ForeignKey('CompanySupervisor', on_delete=models.SET_NULL,null=True, blank=True)
    university_supervisor = models.ForeignKey('UniversitySupervisor', on_delete=models.SET_NULL,null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    week_number = models.IntegerField(null=True, blank=True)
    date = models.DateField(max_length=50,null=True, blank=True)
    report_details = models.TextField(max_length=50,null=True, blank=True)

class Company(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50,null=True, blank=True)
    comp_id = models.CharField(max_length=50,null=True, blank=True)

class CompanyProfile(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE,primary_key=True)
    img = models.ImageField(upload_to="files\\images", null=True, blank=True)
    img_bk = models.ImageField(upload_to="files\\images", null=True, blank=True)
    bio = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50,null=True, blank=True)
    location = models.CharField(max_length=50,null=True, blank=True)

class Post(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    training_mode = models.CharField(max_length=50, choices=[('remote', 'Remote'), ('onsite', 'Onsite')])
    post_details = models.JSONField()
    date = models.DateField(auto_now_add=True)

class CompanySupervisor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    role = models.CharField(max_length=50, null=True, blank=True)

class CompanySupervisorProfile(models.Model):
    company_supervisor = models.OneToOneField(CompanySupervisor, on_delete=models.CASCADE,primary_key=True)
    img = models.ImageField(upload_to="files\\images", null=True, blank=True)
    img_bk = models.ImageField(upload_to="files\\images", null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)

class TrainingApplication(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    company_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    university_supervisor_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    department_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    
    # when the application is approved by all parties a signal will be created to assign the student to the company
    def is_approved(self):
        return self.company_status == 'APPROVED' and self.university_supervisor_status == 'APPROVED' and self.department_status == 'APPROVED'
    
    def approve_by_company(self, user):
        if isinstance(user, Company):
            self.company_status = 'APPROVED'
            self.save()
    def approve_by_university_supervisor(self, user):
        if isinstance(user, UniversitySupervisor):
            self.university_supervisor_status = 'APPROVED'
            self.save()
    def approve_by_department(self, user):
        if user.is_staff:  # assuming department users are staff
            self.department_status = 'APPROVED'
            self.save()

class StudentNotification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


class UniversityNotification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    training_application = models.ForeignKey(TrainingApplication, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)