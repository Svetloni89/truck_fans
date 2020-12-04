# Generated by Django 3.1.3 on 2020-11-12 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck_app', '0008_auto_20201110_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truck',
            name='img_url',
        ),
        migrations.AddField(
            model_name='truck',
            name='image',
            field=models.ImageField(default='', upload_to='public/images'),
            preserve_default=False,
        ),
    ]