from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin,AbstractBaseUser
    
class UserAccountManager(BaseUserManager):
  def create_user(self, email, account_type,password=None):
    if not email:
      raise ValueError('Users must have an email address')

    email = self.normalize_email(email)
    email = email.lower()

    user = self.model(
 
      email=email,
      account_type= account_type
    )

    user.set_password(password)
    user.save(using=self._db)

    return user
  
  def create_superuser(self, email, password=None):
    user = self.create_user(
      email,
      password=password,
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
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPE_CHOICES)
  
    email = models.EmailField(unique=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email



class StudentProfile(models.Model):
    LOCATIONS = (
        ('amman', 'Amman'),
        ('Irbid', 'irbid'),
        ('zarqa', 'Zarqa')
    )
    DEPARTMENTS = (
        ("computer_science","Computer Science"),
    )
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="student",primary_key=True)
    location = models.CharField(max_length=50,choices=LOCATIONS,null=True,blank=True)
    department = models.CharField(max_length=50,choices=DEPARTMENTS, null=True,blank=True)
    phone = models.CharField(blank=True,null=True,max_length=50)
    cv = models.FileField(upload_to="files",null=True,blank=True)
    img= models.ImageField(upload_to="files",null=True,blank=True)
    img_bk=models.ImageField(upload_to="files",null=True,blank=True)
    # put forign key of ids that exsit 
    # img_id=models.CharField(blank=True,null=True,max_length=50)


class UniversitySupervisorProfile(models.Model):
    LOCATIONS = (
        ('amman', 'Amman'),
        ('Irbid', 'irbid'),
        ('zarqa', 'Zarqa')
    )
    DEPARTMENTS = (
        ("computer_science","Computer Science"),
    )
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="University_Supervisor")
    location = models.CharField(max_length=50,choices=LOCATIONS,null=True,blank=True)
    department = models.CharField(max_length=50,choices=DEPARTMENTS, null=True,blank=True)
    phone = models.CharField(blank=True,null=True,max_length=50)
    img= models.ImageField(upload_to="files",null=True,blank=True)
    img_bk=models.ImageField(upload_to="files",null=True,blank=True)

class CompanyProfile(models.Model):
    LOCATIONS = (
        ('amman', 'Amman'),
        ('Irbid', 'irbid'),
        ('zarqa', 'Zarqa')
    )
    
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="Company")
    location = models.CharField(max_length=50,choices=LOCATIONS,null=True,blank=True)
    phone = models.CharField(blank=True,null=True,max_length=50)
    comp_id=models.CharField(blank=True,null=True,max_length=50)
    img= models.ImageField(upload_to="files",null=True,blank=True)
    img_bk=models.ImageField(upload_to="files",null=True,blank=True)

class CompanySupervisorProfile(models.Model):
    LOCATIONS = (
        ('amman', 'Amman'),
        ('Irbid', 'irbid'),
        ('zarqa', 'Zarqa')
    )
    
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="Company_supervisor")
    location = models.CharField(max_length=50,choices=LOCATIONS,null=True,blank=True)
    phone = models.CharField(blank=True,null=True,max_length=50)
    role=models.CharField(blank=True,null=True,max_length=50)
    img= models.ImageField(upload_to="files",null=True,blank=True)
    img_bk=models.ImageField(upload_to="files",null=True,blank=True)




