# Generated by Django 3.0.6 on 2020-06-08 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0022_job_employee'),
        ('users', '0004_invite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invite',
            name='job',
        ),
        migrations.AddField(
            model_name='invite',
            name='job',
            field=models.ManyToManyField(related_name='invites', to='jobs.Job'),
        ),
    ]