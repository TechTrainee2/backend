# Generated by Django 4.2.11 on 2024-04-07 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_companyprofile_img_alter_companyprofile_img_bk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='account_type',
            field=models.CharField(choices=[('STUDENT', 'Student'), ('UNIVERSITY_SUPERVISOR', 'University Supervisor'), ('COMPANY', 'Company'), ('COMPANY_SUPERVISOR', 'Company Supervisor'), ('DEPARTMENT', 'Department'), ('REGISTRATION', 'Registration'), ('ADMIN', 'Admin')], default='ADMIN', max_length=50),
        ),
    ]