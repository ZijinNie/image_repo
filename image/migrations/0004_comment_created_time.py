# Generated by Django 3.1.5 on 2021-01-15 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_image_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
