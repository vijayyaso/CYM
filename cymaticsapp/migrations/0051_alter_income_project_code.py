# Generated by Django 4.0.1 on 2024-08-08 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cymaticsapp', '0050_alter_income_project_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='project_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='income_income', to='cymaticsapp.project'),
        ),
    ]
