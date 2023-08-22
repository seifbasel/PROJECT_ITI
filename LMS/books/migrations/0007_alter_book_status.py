# Generated by Django 4.2.4 on 2023-08-22 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0003_remove_status_desc'),
        ('books', '0006_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.ForeignKey(default='Availlable', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='status.status'),
        ),
    ]
