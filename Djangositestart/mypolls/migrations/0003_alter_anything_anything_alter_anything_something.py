# Generated by Django 5.0.1 on 2024-02-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypolls', '0002_anything'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anything',
            name='anything',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='anything',
            name='something',
            field=models.CharField(max_length=10),
        ),
    ]
