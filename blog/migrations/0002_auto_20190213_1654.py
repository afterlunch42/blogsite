# Generated by Django 2.1.7 on 2019-02-13 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='last_create_time',
            new_name='last_updated_time',
        ),
    ]