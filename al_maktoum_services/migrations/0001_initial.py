# Generated by Django 5.1 on 2025-01-27 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('supervisor_name', models.CharField(max_length=255)),
                ('supervisor_contact', models.CharField(max_length=20)),
                ('project_type', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_spent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('particular', models.TextField()),
                ('transaction_date', models.DateField()),
                ('receipt', models.FileField(blank=True, null=True, upload_to='receipts/')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='al_maktoum_services.project')),
            ],
        ),
    ]
