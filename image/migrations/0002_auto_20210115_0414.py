# Generated by Django 3.1.5 on 2021-01-15 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageentity',
            name='picture',
            field=models.ImageField(blank=True, max_length=500, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='imageentity',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image.image'),
        ),
    ]