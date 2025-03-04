# Generated by Django 5.0 on 2024-12-29 17:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genre', '0001_initial'),
        ('status', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='books/images')),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('borrow_date', models.DateField(blank=True, null=True)),
                ('borrow_period', models.IntegerField(blank=True, null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='genre.genre')),
                ('status', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='status.status')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
