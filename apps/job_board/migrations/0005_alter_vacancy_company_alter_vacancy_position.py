# Generated by Django 4.2.1 on 2023-05-19 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0004_vacancy_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='job_board.company'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='position_vacancies', to='job_board.positiontype'),
        ),
    ]
