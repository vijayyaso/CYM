# Generated by Django 4.0.1 on 2024-07-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cymaticsapp', '0012_alter_project_pending_amt_alter_project_profit'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
