# Generated by Django 3.0.6 on 2020-05-30 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0017_auto_20200531_0025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]