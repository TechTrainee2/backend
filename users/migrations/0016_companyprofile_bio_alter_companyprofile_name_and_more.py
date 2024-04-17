# Generated by Django 4.2.11 on 2024-04-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_remove_studentprofile_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='bio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='companysupervisorprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='companysupervisorprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='universitysupervisorprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='universitysupervisorprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
