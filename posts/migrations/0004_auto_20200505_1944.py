# Generated by Django 2.2 on 2020-05-06 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_published_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_date', '-updated_at', '-created_at']},
        ),
    ]
