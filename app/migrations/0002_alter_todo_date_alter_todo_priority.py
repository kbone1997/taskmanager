# Generated by Django 4.2.1 on 2023-09-26 08:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('1', 'High'), ('2', 'Medium'), ('3', 'Low')], max_length=6),
        ),
    ]