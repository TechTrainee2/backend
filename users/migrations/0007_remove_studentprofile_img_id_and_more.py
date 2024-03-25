# Generated by Django 5.0.3 on 2024-03-24 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_studentprofile_img_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='img_id',
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='img_bk',
            field=models.ImageField(blank=True, null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='companysupervisorprofile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='companysupervisorprofile',
            name='img_bk',
            field=models.ImageField(blank=True, null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='img_bk',
            field=models.ImageField(blank=True, null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='universitysupervisorprofile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='universitysupervisorprofile',
            name='img_bk',
            field=models.ImageField(blank=True, null=True, upload_to='files'),
        ),
    ]
