# Generated by Django 5.0.3 on 2024-04-22 12:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_companyprofile_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='universitysupervisorprofile',
            name='id',
        ),
        migrations.AlterField(
            model_name='universitysupervisorprofile',
            name='university_supervisor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.universitysupervisor'),
        ),
    ]
