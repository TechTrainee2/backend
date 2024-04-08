# Generated by Django 4.2.11 on 2024-04-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_companyprofile_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='files\\images'),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='img_bk',
            field=models.ImageField(blank=True, null=True, upload_to='files\\images'),
        ),
        migrations.AlterField(
            model_name='companysupervisorprofile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='files\\images'),
        ),
        migrations.AlterField(
            model_name='companysupervisorprofile',
            name='img_bk',
            field=models.ImageField(blank=True, null=True, upload_to='files\\images'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='files\\cvs'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='files\\images'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='img_bk',
            field=models.ImageField(blank=True, null=True, upload_to='files\\images'),
        ),
        migrations.AlterField(
            model_name='universitysupervisorprofile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='files\\images'),
        ),
        migrations.AlterField(
            model_name='universitysupervisorprofile',
            name='img_bk',
            field=models.ImageField(blank=True, null=True, upload_to='files\\images'),
        ),
    ]
