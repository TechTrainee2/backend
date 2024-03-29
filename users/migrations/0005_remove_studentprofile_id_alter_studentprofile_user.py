# Generated by Django 5.0.3 on 2024-03-24 19:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_studentprofile_img_studentprofile_img_bk_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='id',
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='student', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]