# Generated by Django 4.2.1 on 2023-09-26 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_todo_date_alter_todo_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
    ]
