# Generated by Django 5.0.3 on 2024-05-29 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='state',
        ),
    ]
