# Generated by Django 4.2.1 on 2023-09-24 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('C', 'Completed'), ('P', 'Pending')], max_length=2)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('C', 'Completed'), ('P', 'Pending')], max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
