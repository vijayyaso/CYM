# Generated by Django 4.0.1 on 2024-08-08 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cymaticsapp', '0046_remove_project_expenses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='image',
        ),
        migrations.AlterField(
            model_name='income',
            name='project_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to='cymaticsapp.project'),
        ),
    ]
