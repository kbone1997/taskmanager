# Generated by Django 4.2.1 on 2023-09-26 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_todo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
