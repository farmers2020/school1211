# Generated by Django 2.2.3 on 2019-08-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app33', '0004_studentsmarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='Regno',
            field=models.CharField(default=False, max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='students',
            name='Regno',
            field=models.CharField(default=False, max_length=30, primary_key=True, serialize=False),
        ),
    ]
