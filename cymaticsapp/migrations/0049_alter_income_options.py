# Generated by Django 4.0.1 on 2024-08-08 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cymaticsapp', '0048_alter_income_project_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='income',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Incomes'},
        ),
    ]
