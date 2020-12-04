# Generated by Django 3.1.3 on 2020-11-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('img_url', models.URLField()),
            ],
        ),
    ]
