# Generated by Django 4.0.10 on 2024-07-15 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=25)),
                ('userNumber', models.CharField(max_length=10)),
                ('userEmail', models.EmailField(max_length=25, unique=True)),
                ('userPass', models.CharField(max_length=25)),
            ],
        ),
    ]
