# Generated by Django 2.0.3 on 2018-03-31 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='isGrayscaled',
            field=models.BooleanField(default=False),
        ),
    ]
