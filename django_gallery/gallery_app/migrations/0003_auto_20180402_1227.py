# Generated by Django 2.0.3 on 2018-04-02 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0002_picture_isgrayscaled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='name',
        ),
        migrations.AddField(
            model_name='picture',
            name='picture',
            field=models.ImageField(default=None, upload_to='images'),
        ),
    ]
