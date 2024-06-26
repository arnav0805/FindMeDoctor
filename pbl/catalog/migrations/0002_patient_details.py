# Generated by Django 4.2.7 on 2023-11-03 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.FloatField(default=0.0)),
                ('phone_number', models.IntegerField(default=0)),
                ('locations', models.CharField(max_length=300)),
            ],
        ),
    ]
