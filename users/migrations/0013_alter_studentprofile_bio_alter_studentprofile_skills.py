# Generated by Django 5.0.3 on 2024-04-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_studentprofile_bio_studentprofile_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
    ]
