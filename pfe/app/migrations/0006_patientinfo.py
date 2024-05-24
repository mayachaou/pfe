# Generated by Django 5.0.3 on 2024-05-22 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_patient_sexe'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('sexe', models.CharField(max_length=20)),
            ],
        ),
    ]
