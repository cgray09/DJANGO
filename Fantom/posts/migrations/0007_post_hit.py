# Generated by Django 3.0.6 on 2020-05-22 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_slider_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
