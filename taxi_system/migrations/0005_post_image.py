# Generated by Django 3.2 on 2021-05-19 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_system', '0004_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to='poster/'),
            preserve_default=False,
        ),
    ]