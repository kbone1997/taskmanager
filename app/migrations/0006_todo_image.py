# Generated by Django 4.2.1 on 2023-09-26 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_todo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
