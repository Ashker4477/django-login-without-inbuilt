# Generated by Django 3.1.3 on 2020-11-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fn', models.CharField(max_length=100)),
                ('ln', models.CharField(max_length=100)),
                ('em', models.CharField(max_length=100)),
                ('Dob', models.DateTimeField()),
            ],
        ),
    ]
