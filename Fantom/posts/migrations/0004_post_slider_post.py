# Generated by Django 3.0.6 on 2020-05-20 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200521_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slider_post',
            field=models.BooleanField(default=False),
        ),
    ]