# Generated by Django 3.0.6 on 2020-05-20 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_slider_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slider_post',
            field=models.BooleanField(default=False),
        ),
    ]