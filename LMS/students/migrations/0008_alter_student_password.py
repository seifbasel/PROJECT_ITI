# Generated by Django 4.2.4 on 2023-08-21 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(default=1234, max_length=255),
        ),
    ]
