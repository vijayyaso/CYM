# Generated by Django 5.1 on 2024-09-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cymaticsapp', '0056_alter_entertainment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
