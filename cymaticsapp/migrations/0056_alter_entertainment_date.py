# Generated by Django 5.1 on 2024-09-02 14:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cymaticsapp', '0055_expense_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
