# Generated by Django 4.2.1 on 2023-05-23 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0005_jobseekerprofile_company'),
        ('job_board', '0006_vacancyresponses_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancyresponses',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='left_responses', to='auth_app.jobseekerprofile'),
        ),
        migrations.AlterField(
            model_name='vacancyresponses',
            name='vacancy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_responded', to='job_board.vacancy'),
        ),
    ]
