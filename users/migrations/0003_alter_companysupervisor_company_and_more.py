# Generated by Django 5.0.3 on 2024-04-20 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_student_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companysupervisor',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.company'),
        ),
        migrations.AlterField(
            model_name='universitysupervisor',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.department'),
        ),
    ]
