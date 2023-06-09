# Generated by Django 4.2.1 on 2023-05-26 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0010_vacancy_is_closed_delete_employee'),
        ('auth_app', '0006_employee_alter_user_account_type_employeeprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employees', to='job_board.company'),
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='position',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='job_board.positiontype'),
        ),
    ]
